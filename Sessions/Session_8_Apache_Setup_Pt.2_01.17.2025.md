# Configure Apache image
# Deploy Apache container and connect it with Flask container.

### Removed the apache configuration file

### Troubleshoot the flask container

Flask container kept closing upon deployment.  
We used the same configuration that worked previously to no effect.  
After many unsuccessful attempts to deploy the container, we looked through each file associated with the project.  
The App.py file we created days prior had some changes that we concluded affected the flask container.  
We deleted the changes within the App.py file and was successful with deploying the flask container.

### Connect apache and flask containers using the docker network command

