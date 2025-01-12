# Flask Documenation

https://flask.palletsprojects.com/en/stable/installation/

## Python Version

Flask supports Python 3.9 and newer

### Dependencies

These distributions will be installed automatically when installing Flask.
Werkzeug implements WSGI, the standard Python interface between applications and servers.
Jinja is a template language that renders the pages your application serves.
MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
ItsDangerous securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
Click is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.
Blinker provides support for Signals

### Project structure:
![image](https://github.com/user-attachments/assets/87ca2d13-90d4-47fc-9ff0-686816b0df81)

#### Python/Flask with Apache proxy and MariaDB database


![image](https://github.com/user-attachments/assets/57b071c0-d8b6-413b-bd3a-965003b12185)




Example project for reference: https://github.com/docker/awesome-compose/tree/master/nginx-flask-mysql

### Issues exprienced:

Created webapp directory in the root directory of our Server and expirenced issues when attempting to run docker build.

```
2025-01-11T20:12:18Z docker.dockerd[1111]: time="2025-01-11T20:12:18.455086793Z" level=error msg=/moby.buildkit.v1.Control/Solve error="rpc error: code = Unknown desc = failed to read dockerfile: open Dockerfile: no such file or directory"
```

We attempted to change the permissions of the directory to no success

The issue was related to the snap package manager version of docker.

Removed docker and reinstalled from the official repo: https://docs.docker.com/engine/install/ubuntu/

## Dockerfile for Flask application
```
# Installs alpine version 3.21
FROM alpine:3.21

# Create a working directory in the image
WORKDIR /app

# Copies files from host directory to /app directory in image
COPY . /app

# Install python latest version and pip
RUN apk add --no-cache python3 py3-pip

# Create virtual environment, activates the environment and installs flask
RUN python3 -m venv /venv && . /venv/bin/activate && pip install Flask

# Sets path to the virtual environment
ENV PATH="/venv/bin:$PATH"

# Runs Flask application. Did not have to specify the app file since by default it uses app.py, which we decided to name our file.

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

```

## app.py (Hello,Wolrd! application)
````
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

````

## Note

### multi-platform environments:

The --platform flag indicates the platform (e.g., linux/amd64, linux/arm64) on which the build should run.

$BUILDPLATFORM is a Docker BuildKit variable that dynamically resolves to the architecture and operating system of the machine performing the build.

This ensures the base image is compatible with the build platform. For instance:
On an amd64 machine, python:3.10-alpine for amd64 will be pulled.
On an arm64 machine, the equivalent python:3.10-alpine for arm64 will be pulled, if available.

Example: 
FROM --platform=$BUILDPLATFORM python:3.10-alpine

Reference document: https://docs.docker.com/build/building/multi-platform/
