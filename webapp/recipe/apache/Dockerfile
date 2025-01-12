# Build image using httpd alpine 3.21
FROM httpd:alpine3.21

COPY httpd.conf /usr/local/apache2/conf/httpd.conf

CMD ["sh", "-c", "httpd -k restart && httpd -D FOREGROUND"]
