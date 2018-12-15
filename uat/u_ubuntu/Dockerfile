FROM ubuntu:18.04

RUN apt-get update; apt-get upgrade -y

RUN apt-get install -y python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev 
RUN apt-get install -y python-mysqldb mysql-client libmysqlclient-dev

RUN apt-get install -y curl telnet dnsutils
RUN apt-get install -y mysql-utilities

RUN pip install --upgrade pip
RUN pip install --upgrade dj-database-url regex
RUN pip install --upgrade sqlalchemy MySQL-python
RUN pip install pandas==0.21.0
RUN pip install pandas_datareader==0.5.0


######

RUN apt-get install -y build-essential
RUN apt-get install -y python-setuptools python-dev
RUN apt-get install -y python-pip

RUN apt-get install -y gfortran libopenblas-dev liblapack-dev
RUN apt-get install -y pkg-config
RUN apt-get install -y wget

RUN pip install numpy
RUN pip install scipy
RUN pip install pandas
RUN pip install patsy
RUN pip install statsmodels
RUN apt-get install -y libfreetype6-dev; \
	pip install matplotlib
RUN pip install ws4py
RUN pip install tornado
RUN pip install tweepy
RUN pip install cython
RUN pip install retrying

# TA-Lib
RUN cd /tmp; \
	wget http://sourceforge.net/projects/ta-lib/files/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz; \
	tar -xzf ta-lib-0.4.0-src.tar.gz; \
	cd ta-lib; \
	./configure ; make; make install; \
	cd ..; \
	rm ta-lib-0.4.0-src.tar.gz; \
	rm -rf ta-lib
RUN pip install TA-Lib

RUN pip install pyalgotrade==0.20
