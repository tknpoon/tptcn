FROM ubuntu:16.04

RUN apt-get update; apt-get upgrade -y
RUN apt-get install -y python-pip

RUN pip install --upgrade pip
RUN pip install --upgrade telepot 

COPY telegram.py /telegram.py 

EXPOSE 1025

