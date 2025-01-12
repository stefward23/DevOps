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
