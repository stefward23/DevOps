# Installs alpine version 3.21
FROM alpine:3.21

# Create a working directory in the image
WORKDIR /app

# Copies files from host directory to /app directory in image
COPY . /app

# Install python3, pip and necessary dependencies
RUN apk add --no-cache python3 py3-pip

# Create virtual environment and install flask
RUN python3 -m venv /venv && \
    /venv/bin/pip install Flask

# Set the virtual environment's bin directory as the PATH
ENV PATH="/venv/bin:$PATH"

# Set the Flask application file (if needed)
ENV FLASK_APP=app.py

# Expose port 5000 for Flask
EXPOSE 5000

# Run Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

