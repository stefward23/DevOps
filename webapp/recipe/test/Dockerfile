# Build image using httpd alpine 3.21
FROM httpd:alpine3.21 AS build

CMD ["httpd", "-D", "FOREGROUND"]

RUN httpd -t
