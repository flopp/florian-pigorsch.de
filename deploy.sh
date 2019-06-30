#!/bin/bash

set -euo pipefail

. config.txt
ssh $SERVER mkdir -p $BASE
rsync -avz --progress deploy/. $SERVER:$BASE
