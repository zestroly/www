#!/bin/sh
PATH=/bin:/sbin:/usr/bin:/usr/sbin
saveTempXmlFile=../xml/temp.xml

`rm -rf $saveTempXmlFile`

while read temp
do
    echo $temp >>$saveTempXmlFile
done

`/home/root/bin/XiXmlDevice set $saveTempXmlFile > /dev/null`

echo -e "Content-type:text/json \n\n"
echo ""
echo "{\"Msg\":\"Setting XmlFile ok!\"}"
