#!/bin/bash

sudo docker run -d \
  -p 443:8888 \
  -v $HOME/workspace/data_science:/notebooks \
  -e "PASSWORD=datasci" \
  --name ipython-notebook \
  ipython-notebook

sudo docker exec -t -i ipython-notebook /bin/bash
