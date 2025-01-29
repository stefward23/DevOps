# Configure SSH to Github repo 5hrs

### Stefan:

Modified file session 1 file from docx to .md format  
Generated ssh keys

Link: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

## Added ssh keys to GitHub
![image](https://github.com/user-attachments/assets/2dfa4b28-e3a7-4c3c-a611-03f002937288)

## Cloned repository from GitHub using gitbash
```
git clone git@github.com:stefward23/DevOps.git
```
![image](https://github.com/user-attachments/assets/0c1b4f0d-9c38-4916-ba3f-67f616973a9d)

## Created a test .md file to test pushing to remote repository
```
git push 
```
**Note: Did not have to specify an upstream branch**

If we did, 
```
git push origin main
```

Tested ssh to Dope's system: ssh techd@techd.ddnsking.com

Ssh connected successfully

Copied public key to server: Failed!

### Akeem:

Created new user "bobby" 

Created home folder for user bobby

Changed user, group and other permissions to 750

### Stefan: 

Ssh using new user: bobby@techd.ddnsking.com

Changed user password

