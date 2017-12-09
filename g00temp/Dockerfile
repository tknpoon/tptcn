FROM ubuntu:16.04

RUN apt-get update; apt-get upgrade -y
RUN apt-get install -y python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev python-mysqldb mysql-client

RUN pip install --upgrade pip
RUN pip install --upgrade scrapy telepot dj-database-url regex
RUN pip install --upgrade pandas pandas_datareader

COPY yahoo.py /yahoo.py
