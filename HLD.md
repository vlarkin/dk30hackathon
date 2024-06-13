
## High-Level Solution Design

![Image](/images/solution_design2.png)

### Description

The initial solution design is based on using GitOps tools to create preview environments from repository branches. Developers create feature branches with changes in the source code. It's easy to automate the tracking of changes in such branches for updating deployed preview environments.

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
