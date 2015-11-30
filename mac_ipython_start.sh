#!/bin/bash

cd $HOME/workspace/data_science
docker stop data-notebook && docker rm data-notebook

docker build -t data-notebook docker/.

docker run -d \
  -p 443:8888 \
  -v $HOME/workspace/data_science:/notebooks \
  -e "PASSWORD=data_science" \
  --name data-notebook \
  --hostname data-notebook \
  data-notebook

docker exec -t -i data-notebook /bin/bash
