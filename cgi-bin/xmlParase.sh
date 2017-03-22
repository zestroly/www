#!/bin/sh
PATH=/bin:/sbin:/usr/bin:/usr/sbin
read temp
data=${temp//\'/\"}

echo -e "Content-type:text/json \n\n"
echo ""
echo `python XmlToJson.py "$data"`
