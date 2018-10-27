FROM vimagick/scrapyd

RUN apt-get update; apt-get upgrade -y
RUN apt-get install -y python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev 
RUN apt-get install -y python-mysqldb mysql-client libmysqlclient-dev

RUN pip install --upgrade pip
RUN pip install --upgrade sqlalchemy MySQL-python
RUN pip install --upgrade mysqlclient

