#!/bin/bash

./build.sh

. config.txt
ssh $SERVER mkdir -p $BASE
rsync -avz --progress deploy/. $SERVER:$BASE
