#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def if_int_to_float(value):
    return value * 1.0 if type(value) == int else value

tree = ET.parse('/Users/rubelw/Downloads/vanbuild.drawio.xml')
root = tree.getroot()

total_cost = 0
total_weight = 0

for item in root.findall('./diagram/mxGraphModel/root/'):
    if item.attrib:
        if 'label' in item.attrib:
            print('label:'+str(item.attrib['label']))
            if 'cost:' in item.attrib['label']:
                lines = str(item.attrib['label']).split("\n")
                for line in lines:
                    if 'cost:' in line:
                        (prefix,suffix) = line.split(':')
                        total_cost = total_cost + float(suffix)
                    if 'weight:' in line:
                        print('###########')
                        (prefix,suffix) = line.split(':')
                        if isinstance(suffix,int):
                            value = if_int_to_float(suffix)
                            total_weight = total_weight + value
                        else:
                            total_weight = total_weight + float(suffix)
print('total cost: '+str(total_cost))
print('total_weight: '+str(total_weight))


