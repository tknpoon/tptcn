FROM ubuntu:16.04

RUN apt-get update; apt-get upgrade -y
RUN apt-get install -y python-pip
RUN apt-get install -y sendemail

RUN pip install --upgrade pip
RUN pip install --upgrade telepot 


COPY telegram.py /telegram.py 
COPY send_telegram.py /send_telegram.py 

EXPOSE 25

