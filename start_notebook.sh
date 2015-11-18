#!/bin/bash

docker run -it \
  --net=host \
  --name=ipython-notebook \
  -p 443:8888 \
  -e "PASSWORD=datasci" \
  -v $HOME/workspace:/notebooks \
  ipython-notebook /bin/bash
