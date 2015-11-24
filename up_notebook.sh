#!/bin/bash

#cd $HOME/workspace/data_science && git pull
sudo docker run -d \
  -p 443:8888 \
  -v $HOME/workspace/data_science:/notebooks \
  -e "PASSWORD=data_science" \
  --name scipyserver \
  ipython/scipyserver

sudo docker exec -t -i scipyserver /bin/bash
