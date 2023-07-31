# Use a base image with Python 3.9 installed
FROM python:3.10-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install gcc -y

# Set working directory
WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# export env
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

# Set the command to run your project
CMD [ "python", "./src/main.py", "-a" ]
