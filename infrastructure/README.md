
# Provisioning infrastructure for preview environments

This Terraform code provisions a GKE cluster and a VM instance. The Ubuntu VM instance is required for running a Slack bot application that manages preview environments in the GKE cluster.  

## Deploying the infrastructure

Everything can be easily set up with the provided commands below. 
Replace <PROJECT_ID> with your actual GCP project ID, <REGION> with the name of the region where you want to deploy the new infrastructure, and <BUCKET_NAME> with a unique name for storing the Terraform state file. 

```
export PROJECT_ID=<PROJECT_ID>
export REGION=<REGION>
export TERRAFORM_BUCKET_NAME=<BUCKET_NAME>

gcloud config set project ${PROJECT_ID}

gsutil mb -c standard -l ${REGION} gs://${TERRAFORM_BUCKET_NAME}
gsutil versioning set on gs://${TERRAFORM_BUCKET_NAME}

terraform init
terraform apply
```

After applying the Terraform code, you should get a Kubernetes cluster and an Ubuntu VM instance.

## Deploying ArgoCD Server to the Kubernetes cluster

Create a namespace for ArgoCD:
```
kubectl create namespace argocd
```

Apply the ArgoCD installation manifest:
```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Change the argocd-server service type to LoadBalancer:
```
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
```

Get initial admin password from the ArgoCD server:
```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}"|base64 -d;echo
```

Setup access to ArgoCD server UI:
```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Navigate to https://127.0.0.1:8080 using login 'admin' and the initial password for checking ArgoCD server status.

## Installing ArgoCD CLI on the VM instance

Get the latest version of ArgoCD CLI:
```
VERSION=$(curl --silent "https://api.github.com/repos/argoproj/argo-cd/releases/latest" | grep '"tag_name"' | sed -E 's/.*"([^"]+)".*/\1/')
```

Download ArgoCD CLI:
```
curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/download/$VERSION/argocd-linux-amd64
```

Make the ArgoCD CLI executable:
```
chmod +x /usr/local/bin/argocd
```

Check the ip address of argocd-server:
```
kubectl get svc argocd-server -n argocd
```

Login to the ArgoCD
```
argocd login *ip_address* --username admin --password $(kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d) --insecure
```

## Installing a Slack Bot Application on the VM Instance

Instructions on how to install, set up, and run Slack Machine are provided [here](/slack-bot/README.md)

