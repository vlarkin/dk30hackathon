
# This is a mock project for testing in preview environments


This project features simple frontend and backend services. The backend is connected to a PostgreSQL database and a Redis cache. The frontend displays the versions of the backend service, the database engine, and the cache engine that the backend service is connected to.


## Deploying the project

This project can be deployed multiple times in different namespaces within a Kubernetes cluster. Create a namespace and use a Helm chart to deploy the project.

```
kubectl create namespace project-name
helm install project-name helm/ -n project-name
```

Finally, it creates an ingress to expose the frontend service with a name like 'project-name.test.env'. After 2-3 minutes, the ingress should be ready to serve requests. You can get the IP address assigned to the ingress and bind it to the ingress host 'project-name.test.env' in /etc/hosts.

```
NAMESPACE=project-name.test.env; echo "$(kubectl get ingress --namespace ${NAMESPACE} \
         -o jsonpath='{.items[*]..status.loadBalancer.ingress[*].ip}') ${NAMESPACE}.test.env" | sudo tee -a /etc/hosts
```

Navigate to http://project-name.test.env to view the project's frontend output.

