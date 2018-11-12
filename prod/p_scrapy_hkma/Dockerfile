FROM vimagick/scrapyd

RUN apt-get update; apt-get upgrade -y
RUN apt-get install -y python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev python-mysqldb mysql-client
RUN apt-get install -y default-libmysqlclient-dev

RUN pip install --upgrade pip
RUN pip install --upgrade sqlalchemy
RUN pip install --upgrade MySQL-python
RUN pip install --upgrade mysqlclient

