# Use Alpine as the base image
FROM alpine:latest

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3 
RUN pip install --upgrade pip --break-system-packages
# Install additional local dependencies and run the test script
RUN pip --no-cache-dir install -r requirements.local.txt --break-system-packages

# Set the default command to run your app
CMD ["python3", "venv/test.py"]