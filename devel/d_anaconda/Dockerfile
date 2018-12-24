FROM ubuntu:18.04

# Updating Ubuntu packages
RUN apt-get update && apt-get upgrade -y 

RUN apt-get install -y wget p7zip-full unzip bzip2 sudo
RUN apt-get install -y build-essential

RUN cd /tmp && wget --quiet http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz -O- | tar xzf -
RUN cd /tmp/ta-lib/ ;./configure; make; make install ; rm -rf /tmp/ta-lib

# Add user ubuntu with no password, add to sudo group
RUN adduser --disabled-password --gecos '' ubuntu
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu
WORKDIR /home/ubuntu/
RUN chmod a+rwx /home/ubuntu/

# Anaconda installing
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda2-5.3.1-Linux-x86_64.sh -O- > ~/anaconda.sh && bash ~/anaconda.sh -b && rm ~/anaconda.sh
#RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh -O- > ~/anaconda.sh && bash ~/anaconda.sh -b && rm ~/anaconda.sh

# Set path to conda
 ENV PATH /home/ubuntu/anaconda2/bin:$PATH
#ENV PATH /home/ubuntu/anaconda3/bin:$PATH

# Updating Anaconda packages
RUN conda install PyMySql
RUN pip install TA-Lib PyAlgoTrade
#RUN conda update anaconda
### RUN conda update --all

# Configuring access to Jupyter

EXPOSE 8888
RUN mkdir /home/ubuntu/notebooks
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password = u'sha1:fe1698e7a652:4e05f2b1a694074e87e35039be56114c703e2a6f'" >> /home/ubuntu/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.quit_button = False" >> /home/ubuntu/.jupyter/jupyter_notebook_config.py

