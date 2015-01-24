#!/bin/bash

. config.txt

staticjinja build --outpath=deploy

sed -e "s#BASEURL#http://www.florian-pigorsch.de#g" -e "s/TIMESTAMP/$(date +%Y-%m-%dT%H:%M:%S%:z)/g" src/sitemap.xml > deploy/sitemap.xml

ncftpput -u $LOGIN -p $PASSWD -R $SERVER $BASE/ deploy/*
