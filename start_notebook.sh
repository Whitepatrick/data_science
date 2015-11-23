#!/bin/bash

cd $HOME/workspace/data_science && git pull

sudo docker build -t ipython-notebook docker/.
sudo docker run -d \
  -p 443:8888 \
  -v $HOME/workspace/data_science:/notebooks \
  -e "PASSWORD=datasci" \
  --name ipython-notebook \
  ipython-notebook

sudo docker exec -t -i ipython-notebook /bin/bash
