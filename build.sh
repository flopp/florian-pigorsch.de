#!/bin/bash

staticjinja build --outpath=deploy
sed -e "s#BASEURL#https://www.florian-pigorsch.de#g" -e "s/TIMESTAMP/$(date +%Y-%m-%dT%H:%M:%S%:z)/g" src/sitemap.xml > deploy/sitemap.xml
