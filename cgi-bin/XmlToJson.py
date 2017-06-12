#!/usr/bin/python3.6

from xml.dom.minidom import parse
import xml.dom.minidom


import os
import sys,json


json_str=sys.argv[1]
#print(json_str)
#print(type(json_str))
json_dict=json.loads(json_str)
xmlstr = ""

for key in json_dict:
    if(key == 'data'):
        break;
    xmlstr +="<Param ErrorCode=\"0\">"
    xmlstr += "<camera>"
    xmlstr += "<" + key + ">"
    for i in json_dict[key]:
        xmlstr += "<" + i + " "
        for j in json_dict[key][i]:
            xmlstr +=" " + j + "=\"" +json_dict[key][i][j] + "\""
        xmlstr += "/>"
    xmlstr += "</" + key + ">"
    xmlstr += "</camera>"
    xmlstr += "</Param>"
    f=open('/tmp/temp.xml', 'w')
    f.write(xmlstr);
    f.close();
    os.system("/home/root/bin/XmlDevice set /tmp/temp.xml > /dev/null")

os.system("/home/root/bin/XiXmlDevice get /home/root/config/camera.xml > /dev/null")


DOMTree = xml.dom.minidom.parse("/home/root/config/camera.xml")
root=DOMTree.documentElement
cameraNodes=root.getElementsByTagName('camera')


def getAttrbute(node):
    tempstr="{"
    j=1
    for key in node.attributes.keys():
        tempstr += "\""+ key+"\":\""+node.attributes[key].value+"\""
        if j < (node.attributes.length):
            tempstr +=","
        j=j+1
    tempstr+="}"
    return  tempstr





def metaNode(cells, str):
    str +="\""+cells.nodeName+"\"" + ":"
    str+='{'
    i=0
    for cell in cells.childNodes:
        i=i+1
        if cell.nodeType == 3:
            continue
        str += "\""+cell.nodeName+"\"" + ":"
        str += getAttrbute(cell)
        if i < (cells.childNodes.length-1):
            str +=","
    str += "}"
    return str


str="{"

for camerchild in cameraNodes:
    k=0
    for cell in camerchild.childNodes:
        k=k+1
        if cell.nodeType == 3:
            continue
        str = metaNode(cell,str)
        if k < (camerchild.childNodes.length-1):
            str += ","

str+="}"

print (str)


