# Used vscode to ssh into a remote computer.

### Akeem:
Attempted to run docker from non root users.  
Gave away root privileges to all users like a bot.  
Create a docker group and added users to it.  
Copied .bashrc file to bobby.  
Added LS_COLORS to the .bashrc file.  
Changed owner and group of .bashrc file to bobby:bobby  
Failed!\
## Added Aliases manually
```
alias egrep='egrep --color=auto'  
alias fgrep='fgrep --color=auto'  
alias grep='grep --color=auto'  
```
Failed!

### Both:
Tried to push a docker image to the repo

## how to login to docker
```
docker login -<username>
```
## see docker images
docker images (to see local images)
```
docker tag <image_name>:<image_tag> <user_name>/<repo_name>:<new_tag>
```
```
docker pull <repo_name>/<image_name>:<image_tag>
```
```
docker push <repo_name>:<tag_name>
```
```
docker rmi <image_name>:<tag_name>
```
## add collaborator

to push to collabs repo

```
docker tag <image_name>:<tag_name> <ex_repo_name>:<tag_name>
```
```
docker push <ex_repo_name>
```
```
docker search <username> 
```

# to search for docker image tags
curl -s https://registry.hub.docker.com/v2/repositories/dopeignite/stefmward/tags | jq '.results[].name'
