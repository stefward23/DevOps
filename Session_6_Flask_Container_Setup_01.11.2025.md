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

#### Python/Flask with Apache proxy and MariaDB database
```
.
├── compose.yaml
├── flask
│   ├── Dockerfile
│   ├── requirements.txt
│   └── server.py
└── nginx
    └── apache2.conf 
```

Example project for reference: https://github.com/docker/awesome-compose/tree/master/nginx-flask-mysql

## multi-platform environemtns:

syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

The --platform flag indicates the platform (e.g., linux/amd64, linux/arm64) on which the build should run.

$BUILDPLATFORM is a Docker BuildKit variable that dynamically resolves to the architecture and operating system of the machine performing the build.

This ensures the base image is compatible with the build platform. For instance:
On an amd64 machine, python:3.10-alpine for amd64 will be pulled.
On an arm64 machine, the equivalent python:3.10-alpine for arm64 will be pulled, if available.

Reference document: https://docs.docker.com/build/building/multi-platform/
