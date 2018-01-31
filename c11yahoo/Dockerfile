FROM ubuntu:latest

RUN apt-get update; apt-get upgrade -y

RUN apt-get install -y python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev python-mysqldb mysql-client libmysqlclient-dev

RUN pip install --upgrade pip
RUN pip install --upgrade scrapy telepot dj-database-url regex
RUN pip install --upgrade pandas pandas_datareader
RUN pip install --upgrade sqlalchemy MySQL-python

