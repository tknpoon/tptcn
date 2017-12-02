# tptcn
## Assumption: Ubuntu 16.04 / user= ubuntu

[ ! -d ~/repo ] && mkdir ~/repo; cd ~/repo; git clone https://github.com/tknpoon/tptcn

curl -fsSL https://github.com/tknpoon/tptcn/raw/master/00mkswap.sh | sudo /bin/bash -

curl -fsSL https://github.com/tknpoon/tptcn/raw/master/01install_docker.sh | sudo /bin/bash -


#End
