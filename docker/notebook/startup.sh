#!/bin/bash
sudo docker build -t notebook .

sudo docker run -t \
  --name="notebook" \
  -p 443:8888 \
  --restart=on-failure:3 \
  -e "PASSWORD=datasci" \
  -v ~/workspace/data_science/:/notebooks \
  -w="/notebooks" \
  notebook
