from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import command
import subprocess
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import re

def sanitize_name(name):
    """Sanitize the given name to make it a valid Kubernetes resource name."""
    name = name.lower()
    name = re.sub(r'[^a-z0-9-]', '-', name)
    name = re.sub(r'(^-+|-+$)', '', name)
    return name

def load_kube_config():
    """Load Kubernetes configuration."""
    try:
        config.load_kube_config()
    except Exception as e:
        raise Exception(f"Failed to load Kubernetes configuration: {str(e)}")

def create_namespace(name):
    """Create a Kubernetes namespace if it does not exist."""
    namespace_name = sanitize_name(name)
    load_kube_config()
    v1 = client.CoreV1Api()
    
    # Check if the namespace already exists
    existing_namespaces = v1.list_namespace()
    for ns in existing_namespaces.items:
        if ns.metadata.name == namespace_name:
            return namespace_name

    # Create the namespace if it does not exist
    namespace = client.V1Namespace(metadata=client.V1ObjectMeta(name=namespace_name))
    try:
        v1.create_namespace(body=namespace)
        return namespace_name
    except ApiException as e:
        raise Exception(f"Exception when creating namespace: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

def create_argocd_application(app_name, team_id, revision):
    """Create an ArgoCD application."""
    try:
        namespace = create_namespace(f"{app_name}-{revision}-{team_id}")
        repo = 'https://github.com/vlarkin/mock-project'
        command = [
            'argocd', 'app', 'create', app_name,
            '--repo', repo,
            '--path', 'helm',
            '--dest-server', 'https://kubernetes.default.svc',
            '--dest-namespace', namespace,
            '--sync-policy', 'automated',
            '--revision', revision
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise Exception(f"Error creating application: {result.stderr.strip()}")
        return result.stdout.strip()
    except Exception as e:
        raise Exception(f"An error occurred while creating application: {str(e)}")

def list_argocd_applications(team_id):
    """List all applications for the given team."""
    try:
        command = ['argocd', 'app', 'list']
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise Exception(f"Error finding applications: {result.stderr.strip()}")

        namespace_pattern = f"-{team_id}"
        apps = []
        for line in result.stdout.splitlines():
            columns = line.split()
            if len(columns) > 0 and namespace_pattern in columns[2]:
                app_name = columns[0].replace('argocd/', '')
                status = columns[4]
                health = columns[5]
                conditions = columns[7]
                namespace = columns[2]
                apps.append((app_name, status, health, conditions, namespace))
        return apps
    except Exception as e:
        raise Exception(f"An error occurred while listing applications: {str(e)}")

def get_ingress_ip(namespace_name):
    """Get the ingress IP for the given namespace."""
    load_kube_config()
    v1 = client.NetworkingV1Api()
    ingress_list = v1.list_namespaced_ingress(namespace=namespace_name)
    ingress_ip_map = {}
    for ingress in ingress_list.items:
        name = ingress.metadata.name
        if ingress.status.load_balancer and ingress.status.load_balancer.ingress:
            for addr in ingress.status.load_balancer.ingress:
                host = ingress.spec.rules[0].host if ingress.spec.rules else None
                ingress_ip_map[name] = (f"http://{host or addr.hostname or addr.ip}", addr.ip)
    return ingress_ip_map

def get_service_name(app_name, namespace_name):
    """Get the service name for the given application and namespace."""
    load_kube_config()
    v1 = client.CoreV1Api()
    service_list = v1.list_namespaced_service(namespace=namespace_name)
    for service in service_list.items:
        if service.metadata.labels and 'app.kubernetes.io/instance' in service.metadata.labels:
            if service.metadata.labels['app.kubernetes.io/instance'] == app_name:
                return service.metadata.name

def get_application_url(app_name, namespace_name):
    """Get the application URL for the given application and namespace."""
    svc = get_service_name(app_name, namespace_name)
    if svc is None:
        return ""
    load_kube_config()
    v1 = client.CoreV1Api()
    service = v1.read_namespaced_service(name=svc, namespace=namespace_name)
    if service.status.load_balancer.ingress:
        for ingress in service.status.load_balancer.ingress:
            if ingress.hostname:
                return f"http://{ingress.hostname}"
            elif ingress.ip:
                return f"http://{ingress.ip}"

def delete_argocd_application(app_name, team_id):
    """Delete the given ArgoCD application and its namespace."""
    try:
        # Get the namespace corresponding to the app
        apps = list_argocd_applications(team_id)
        for app in apps:
            if app[0] == app_name:
                namespace_name = app[4]
                break

        if namespace_name is None:
            raise Exception(f"Namespace corresponding to application '{app_name}' not found.")

        # Construct the command to delete the ArgoCD application
        command = ['argocd', 'app', 'delete', app_name, '--cascade', '--yes']

        # Execute the command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check the result of the command execution
        if result.returncode != 0:
            raise Exception(f"Error deleting application: {result.stderr.strip()}")

        # Delete the namespace
        delete_namespace(namespace_name)

        return f"Preview Environment '{app_name}' deleted successfully."
    except Exception as e:
        raise Exception(f"An error occurred while deleting Preview Environment: {str(e)}")


def delete_namespace(namespace_name):
    """Delete the given namespace."""
    try:
        config.load_kube_config()
        v1 = client.CoreV1Api()
        v1.delete_namespace(namespace_name)
    except Exception as e:
        raise Exception(f"An error occurred while deleting namespace: {str(e)}")
class CommandsPlugin(MachineBasePlugin):

    @command("/create")
    async def create(self, command):
        """Handle the /create command to create a new application."""
        try:
            args = command.text.split()
            if len(args) != 2:
                await command.say("Usage: /create app_name branch_name_or_commit_hash")
                return
            app_name, revision = args
            app_result = create_argocd_application(app_name, command.sender.team_id, revision)
            await command.say(f"Create Preview Environment: {app_result}")
        except Exception as e:
            await command.say(str(e))

    @command("/get")
    async def get(self, command):
        """Handle the /get command to list all applications."""
        try:
            namespace_name = sanitize_name(command.sender.team_id)
            apps = list_argocd_applications(namespace_name)
            if apps:
                app_urls = []
                for app in apps:
                    app_name, status, health, conditions, app_namespace = app
                    if namespace_name in app_namespace:
                        ingress_ip_map = get_ingress_ip(app_namespace)
                        url, ip = ingress_ip_map.get(app_namespace, ("", ""))
                        if conditions == "<none>":
                            app_urls.append(f"{app_name} ({status}, {health}):\t {ip} {url}")
                        else:
                            app_urls.append(f"{app_name} ({status}, {health}, {conditions}):\t {ip} {url}")
                await command.say(f"To access the preview environment, run this with privileged permissions\n"
                                  f"Windows - echo ip_env host_env >> %WINDIR%\\System32\\drivers\\etc\\hosts\n"
                                  f"MacOS/Linux - sudo echo ip_env host_env >> /etc/hosts\n" + "\n".join(app_urls))
            else:
                await command.say("Preview Environment not found.")
        except Exception as e:
            await command.say(str(e))

    @command("/delete")
    async def delete(self, command):
        """Handle the /delete command to delete an application."""
        try:
            namespace_name = sanitize_name(command.sender.team_id)
            delete_result = delete_argocd_application(command.text, namespace_name)
            await command.say(delete_result)
        except Exception as e:
            await command.say(str(e))
