# setting up base image
FROM python:3.11.4-slim-bullseye

# prevents python buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# prevents python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# sets up the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions 
WORKDIR /app

# copy files and directories from current directory to WORKDIR
COPY . /app/


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt