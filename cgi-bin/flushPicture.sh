#!/bin/sh
PATH=/bin:/sbin:/usr/bin:/usr/sbin

cd /home/root/bin
`./Picture 5 0 /srv/www/image.bmp > /dev/null`

echo -e "Content-type:text/json \n\n"
echo ""
echo "{\"Msg\":\"update Picture ok!\"}"