#!/bin/bash

cd $HOME/workspace/data_science
docker stop data-notebook && docker rm data-notebook

docker build -t data-notebook docker/.

docker run -d \
  -p 443:8888 \
  -v $HOME/workspace/data_science:/notebooks \
  -v $HOME/workspace/DAT-NYC-29:/notebooks/notebooks/DAT-NYC-29 \
  -e "PASSWORD=data_science" \
  --hostname data-notebook \
  --name data-notebook \
  data-notebook

#docker exec -t -i data-notebook /bin/bash
