
## Architectural Decision Records

![Image](/images/solution_design1.png)

### Description of tools

For developing a Slack bot, [slack-machine](https://github.com/DonDebonair/slack-machine) was utilized. Slack Machine is a simple and extendable Slack bot framework written in Python. It features an intuitive plugin system that enables rapid bot development while facilitating easy code organization.  
  
GitHub Actions automates Docker image builds upon changes in the application set's source code within repository branches. Docker images are stored in GitHub Container Registry. GitHub Actions seamlessly integrates with the source code to automate Docker image builds upon code changes, while GitHub Container Registry provides centralized storage, streamlining development and deployment processes.  
  
The Argo CD tool utilizes Helm charts for deploying applications to a cluster and the application version control system to track changes in the source code for applying these changes across different branches and namespaces. This ensures that developers can preview and test the versions effectively.  

