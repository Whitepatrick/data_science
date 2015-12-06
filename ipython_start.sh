#!/bin/bash

cd $HOME/workspace/data_science
sudo docker stop data-notebook && sudo docker rm data-notebook

sudo docker build -t data-notebook docker/.

sudo docker run -d \
  -p 443:8888 \
  -v $HOME/workspace/data_science:/notebooks \
  -v $HOME/workspace/DAT-NYC-29:/notebooks/notebooks/DAT-NYC-29 \
  -e "PASSWORD=data_science" \
  --name data-notebook \
  --hostname data-notebook \
  data-notebook

#sudo docker exec -t -i data-notebook /bin/bash
