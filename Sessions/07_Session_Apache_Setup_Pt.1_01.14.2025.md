# PT.1 Apache Setup for Reverse Proxy (Flask Application) 2hrs

## Flask apache documentation
https://flask.palletsprojects.com/en/stable/deploying/apache-httpd/

## Started by attempting to create a dockerfile for apline with apache.

````
# Build image using httpd alpine 3.21
FROM httpd:alpine3.21 AS build

COPY httpd.conf /usr/local/apache2/conf/httpd.conf

CMD ["sh", "-c", "httpd -k restart && httpd -D FOREGROUND"]

````

### Added a httpd.conf file to the same folder as the dockerfile with the following contents:

```
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
ProxyPass / http://127.0.0.1:5000/
RequestHeader set X-Forwarded-Proto http
RequestHeader set X-Forwarded-Prefix /
```

### Built the image

````
docker build -t apache .
````
### Started a container from the image

`````
docker run -d -p 80:80 --name apachetest apache
`````
### Container exited soon after starting.

Attempted to troubleshoot while reading documentation to no success.

#Decide to conclude for the night and would try again at a later date since it was late
