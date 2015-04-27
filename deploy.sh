#!/bin/bash

./build.sh

. config.txt
ncftpput -u $LOGIN -p $PASSWD -R $SERVER $BASE/ deploy/*
