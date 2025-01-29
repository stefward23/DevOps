# PT.2 Apache Setup for Reverse Proxy (Flask Application) 
#### Time: 3 hrs

## Deploy Apache container and connect it with Flask container.


### Removed all previous images and containers. Starting with a clean environment

### Issue expierenced when rebuilding image and starting container

We recreated the docker image for the flask application

````
dockerbuild -t flaskapp .
```````
Build ran successfully, no errors.

Attempted to run a container with the image

```````
docker run -d -p 5000:5000 --name testapp flaskapp
```````
Container exited as soon as it started

### Troubleshoot the flask container
  
We used the same configuration that worked previously to no effect.

After many unsuccessful attempts to deploy the container, we looked through each file associated with the project. 

The App.py file we created days prior had some changes that we concluded affected the flask container.  
![image](https://github.com/user-attachments/assets/c63dae7f-ffd3-4290-97d9-e1892b446eef)

We deleted the changes within the App.py file, rebuilt the image and then was successful with deploying the flask container.

### Connect apache and flask containers using the docker network command

We decided to first run both the flask app container and apache container to test connectivity while configuring the proxy. The dockerfile would be created once testing is completed.

### Images being used:

![image](https://github.com/user-attachments/assets/f53a7ded-7ee4-4d55-b7f0-8990e6027ce3)

#### Flaskapp: Created from our dockerfile
#### httpd: image of apache from dockerhub

#### 1: created a netowrk bridge
````
 docker network create -d bridge test-net
````
Result:
ad323105321c   test-net   bridge    local

#### 2: Started a docker container with the flaskapp image
```````
docker run --network=test-net -d -p 5000:5000 flaskapp
```````
#### 3: Started a docker container with the httpd image
`````
docker run --network=test-net -d -p 80:80 httpd
`````
#### 4: Connected to the httpd container
````
docker exec -it 7e4f239xxxxx /bin/bash
````

#### 5: Installed a text editor by running the following commands
```
apt update && apt install vim

```

##### 6: Edited the /usr/local/apache2/conf/httpd.conf

Uncommented as suggested by flask documentation: https://flask.palletsprojects.com/en/stable/deploying/apache-httpd/
![image](https://github.com/user-attachments/assets/e72fde52-dcda-4d65-b881-4c4e7fc37519)

Uncommented the following lines to enable the proxy modules:
```
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
```
Uncommented the following line as well so we could add the configuration needed for the site. We could have placed the information in this file as well but since it had alot of information already, we decided not to.

##### Virtual hosts
```
Include conf/extra/httpd-vhosts.conf
```

#### 6: Added the following entry to the /apache2/conf/extra/httpd-vhosts.conf file 
`````````
<VirtualHost *:80>
    ServerAdmin admin@example.com
    ServerName localhost

    # Proxy settings
    RequestHeader set X-Forwarded-Proto http
    RequestHeader set X-Forwarded-Port "80"

    ProxyPass / http://distracted_shaw:5000/
    ProxyPassReverse / http://distracted_shaw:5000/
</VirtualHost>
````````````

The entry basically informs apache to foward http request to the root "/" on port 80 to the root "/" of "http://distracted_shaw:5000", which is specified in the app.py as the route. 
![image](https://github.com/user-attachments/assets/0427b53e-0bb7-455b-85e1-c9a5f66c7f8a)
 
distracted_shaw is the name of the container. The name was randomly created because we did not specify a name.

Note: Tested using localhost/127.0.0.1 and this failed to make the proxy work.

#### 7: Verified configuration was ok
``````
httpd -t
``````
Result: ![image](https://github.com/user-attachments/assets/6e3b6be6-1b62-4142-8b2b-bdeaa4a7d92e)


Note: When running the command, it reported a error which can be fixed by adding the ServerName entry to /apache2/conf/httpd.conf
![image](https://github.com/user-attachments/assets/518b56c6-6270-4de5-ae48-5cef5fcc366e)



#### 8: Restarted httpd service
``````
httpd -k restart
``````



