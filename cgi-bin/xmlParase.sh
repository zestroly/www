#!/bin/sh
PATH=/bin:/sbin:/usr/bin:/usr/sbin
`cp /home/root/config/camera.xml /srv/www/xml/camera.xml`
`/home/root/bin/XmlDevice get /srv/www/xml/camera.xml > /dev/null`

echo -e "Content-type:text/json \n\n"
echo ""
echo "{\"Msg\":\"update XmlFile ok!\"}"
