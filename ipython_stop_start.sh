#!/bin/bash

cd $HOME/workspace/data_science
sudo docker stop data-notebook && sudo docker rm data-notebook

sudo docker build -t data-notebook .

sudo docker run -d \
  -p 443:8888 \
  -v $HOME/workspace/data_science:/notebooks \
  -e "PASSWORD=data_science" \
  -e TERM="xterm" \
  --name data-notebook \
  --hostname data-notebook \
  data-notebook

sudo docker exec -t -i data-notebook /bin/bash
