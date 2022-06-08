FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

#Update the packages
#Remove var/lib/apt/lists/ to save space
RUN apt-get update
RUN apt-get install -y python-pip
RUN apt-get clean && rm -rf /var/lib/apt/lists/* 

WORKDIR /backend

#First install libs so if the requirements are not changing them Docker Layers are not updated
COPY requirements.txt /backend/

#No cache dir avoid saving .whl and .tar.gz files of python librairies
RUN pip install --no-cache-dir -r /backend/requirements.txt

COPY . /backend/