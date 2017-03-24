#!/bin/sh
PATH=/bin:/sbin:/usr/bin:/usr/sbin

`/home/root/bin/XiXmlDevice get /srv/www/xml/camera.xml > /dev/null`

echo -e "Content-type:text/json \n\n"
echo ""
echo "{\"Msg\":\"update XmlFile ok!\"}"
