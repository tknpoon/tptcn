FROM ubuntu:18.04

RUN apt-get update; apt-get upgrade -y
RUN apt-get install -y python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev python-mysqldb mysql-client
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y mysql-utilities

RUN pip install --upgrade pip
RUN pip install --upgrade dj-database-url regex
RUN pip install --upgrade sqlalchemy MySQL-python
RUN pip install pandas==0.21.0
RUN pip install pandas_datareader==0.5.0

