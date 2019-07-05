#!/bin/python
import xml.etree.ElementTree as ET

masscan_file = 'result.xml'
tree = ET.parse(masscan_file)
root = tree.getroot()

f = open('output.txt', 'w')

counter = 0
for data in root.iter('host'):
    ip = data.find('address').get('addr')
    port = data.find('ports').find('port').get('portid')
    f.write(ip + ':' + port + '\n')
f.close()
