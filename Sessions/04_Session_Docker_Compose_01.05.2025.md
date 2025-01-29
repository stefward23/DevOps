# Discussed Docker compose 3hrs

### Akeem

## Used docker compose to create 2 containers on the same network

Container 1: Apache installed

Container 2: mySQL installed

Downloaded mySQL client on container 1.

Accessed mySQL table information from container 2 using container 1.

Mounted a volume to store files from each container.

# Discussed using apt update command in containers

Decided to go against it. Can cause updates and break system when image is built from Dockerfile/Docker compose file
