
## Architectural Decision Records

![Image](/images/solution_design2.jpg)

### Description of tools

For developing a Slack bot, [slack-machine](https://github.com/DonDebonair/slack-machine) was utilized. Slack Machine is a simple and extendable Slack bot framework written in Python. It features an intuitive plugin system that enables rapid bot development while facilitating easy code organization.  
  
GitHub Actions automates Docker image builds upon changes in the application set's source code within repository branches. Docker images are stored in GitHub Container Registry. GitHub Actions seamlessly integrates with the source code to automate Docker image builds upon code changes, while GitHub Container Registry provides centralized storage, streamlining development and deployment processes.  
  
The Argo CD tool utilizes Helm charts for deploying applications to a cluster and the application version control system to track changes in the source code for applying these changes across different branches and namespaces. This ensures that developers can preview and test the versions effectively.  

### The flow

1. Developers push changes in their branches to a repository stored on GitHub.  
2. A GitHub Actions workflow builds Docker images and pushes them to GitHub Container Registry.  
3. Developers use Slack to interact with the Slack bot.  
4. The Slack bot is connected to the developers' team Slack channel.  
5. The Slack bot receives commands from developers and interacts with the Argo CD server.  
6. The Argo CD server manages preview environments in the Kubernetes cluster.  
7. Each application set in a preview environment pulls Docker images from GitHub Container Registry.  
8. Developers can navigate to a unique preview environment URL to test their changes and new features.  
9. If developers make fixes in the code, the Argo CD server automatically applies changes to deployed preview environments.  
