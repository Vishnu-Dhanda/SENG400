![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Assignment 1 - Vishnu Dhanda 
Docker Image: ```python:3.7```

 Building:
```shell 
docker build -t assignment1 .
```

Running:
```shell
docker run -v servervol:/serverdata assignment1:latest
```
### Method Used

Creation of the volume was done using the command: '''-v servervol:/serverdata'''  This is the volume mounting option. It tells Docker to create a volume named servervol and mount it to the /serverdata directory inside the container. This allows data to persist beyond the container's lifecycle.

### Additional Notes

The Python application code is located in the app directory under assignment1. 

The file text_gen.py contains the logic to generate random text data and manage the random.txt file.


The Dockerfile at the root of the assignment1 directory specifies the instructions to build the Docker image. It installs the necessary packages and sets up the application environment.

Ensure Docker is installed and running on your system before executing the Docker commands.

