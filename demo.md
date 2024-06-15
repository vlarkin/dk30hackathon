

# Automated Preview Environment Management with Slack Bot


## Prepared Infrastructure


![Image1](images/demo1.png)
**Pic.1: A VM instance for running a bot and nodes of a Kubernetes cluster.**
<br>
<br>
<br>
![Image2](images/demo2.png)
**Pic.2: A demo Kubernetes cluster.**
<br>
<br>
<br>
![Image3](images/demo3.png)
**Pic.3: Argo CD components are running.**
<br>
<br>
<br>
![Image4](images/demo4.png)
**Pic.4: Argo CD web UI shows a clean environment.**


## Making Changes and Creating Preview Environments


![Image5](images/demo5.png)
**Pic.5: Create a new branch 'preview1' and add changes.**
<br>
<br>
<br>
![Image6](images/demo6.png)
**Pic.6: Ask the bot to create environments: pe-0 from the 'develop' branch and pe-1 from the 'preview-1' branch.**
<br>
<br>
<br>
![Image7](images/demo7.png)
**Pic.7: The bot has confirmed the creation of the preview environments.**
<br>
<br>
<br>
![Image8](images/demo8.png)
**Pic.8: The components of the preview environments are up and running.**
<br>
<br>
<br>
![Image9](images/demo9.png)
**Pic.9: The Argo CD web UI displaying deployed preview environments.**
<br>
<br>
<br>
![Image10](images/demo10.png)
**Pic.10: Detailed view of a preview environment in the Argo CD web UI.**


## Preview Environments Access and Functionality Check


![Image11](images/demo11.png)
**Pic.11: The bot provided a list of the created environments in response to the '/get' command.**
<br>
<br>
<br>
![Image12](images/demo12.png)
**Pic.12: Preview environment created from the 'develop' branch.**
<br>
<br>
<br>
![Image13](images/demo13.png)
**Pic.13: Preview environment created from the 'preview1' branch with added changes.**


## Further Changes and Automatic Environment Updates


![Image14](images/demo14.png)
**Pic.14: Making additional updates in the 'preview1' branch.**
<br>
<br>
<br>
![Image15](images/demo15.png)
**Pic.15: Docker images are built with each commit to the 'preview' branch.**
<br>
<br>
<br>
![Image16](images/demo16.png)
**Pic.16: A log entry includes both code changes and version updates.**
<br>
<br>
<br>
![Image17](images/demo17.png)
**Pic.17: The Argo CD web UI displays the updated 'pe-1' environment with the latest version.**
<br>
<br>
<br>
![Image18](images/demo18.png)
**Pic.18: Preview environment created from the 'preview1' branch with the latest changes.**


## Deleting Preview Environments


![Image19](images/demo19.png)
**Pic.19: Sending a message to the bot to delete the 'pe-1' environment.**
<br>
<br>
<br>
![Image20](images/demo20.png)
**Pic.20: The bot has confirmed the deletion of both preview environments.**
