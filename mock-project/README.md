
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

## GitHub Actions workflow and branches

In .github/workflows/build.yml, you can find a script for automatically building frontend and backend Docker images after changes are made in branches. Branches can be used for developing new features and building Docker images with those new features without affecting the current Docker images specified in helm/values.yaml in the master branch.  

This project can be deployed to different namespaces from various branches to test new features before merging them into the master or another stable branch. If you deploy multiple versions of the project from different branches using Argo CD, changes in the branches will be automatically deployed and accessible via ingresses."  
