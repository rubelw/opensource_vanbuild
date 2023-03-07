#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import mdutils

def if_int_to_float(value):
    return value * 1.0 if type(value) == int else value

tree = ET.parse('./promaster/vanbuild.drawio.xml')
root = tree.getroot()

print(str(root))
total_cost = 0
total_weight = 0

for item in root.findall('./mxfile/'):
   print('item: '+str(item))

build_items = {}

for item in root.findall('./diagram/mxGraphModel/root/'):
    if item.attrib:
        if 'label' in item.attrib:
            label = None
            print('label:'+str(item.attrib['label']))
            data = {}
            if 'cost:' in item.attrib['label']:

                lines = str(item.attrib['label']).split("\n")
                for line in lines:
                    if not label:
                        label=line
                    if 'cost:' in line:
                        (prefix,suffix) = line.split(':')
                        total_cost = total_cost + float(suffix)
                        data['cost']=float(suffix)

                    if 'weight:' in line:
                        print('###########')
                        (prefix,suffix) = line.split(':')
                        if isinstance(suffix,int):
                            value = if_int_to_float(suffix)
                            total_weight = total_weight + value
                            data['weight'] = value
                        else:
                            total_weight = total_weight + float(suffix)
                            data['weight'] = float(suffix)
                    else:
                        data['weight'] = 0
            build_items[label]= data



mdFile = mdutils.MdUtils(file_name='README',title='Open Source Van Build')
mdFile.new_header(level=1, title='Overview')

mdFile.new_paragraph("This is a repository of a draw.io image of all components needed for an electric van build.")
mdFile.new_paragraph("The intent of this repository is to determine all the components, costs and weights prior to the purchase of an electric van.")
mdFile.new_paragraph("This repository is currently modeled for the future Promaster Electric Vans, but more vans can be added as needed.")
mdFile.new_paragraph("To utilize and customize for your own use, click-on promaster/vanbuild.drawio.xml file and save to your local computer. Then go to https://app.diagrams.net/ and open the file to see all the links, and to modify to your own needs. If you find and error, or issue, please post back to https://github.com/rubelw/opensource_vanbuild/issues")


mdFile.new_header(level=2,title='The design includes:')
mdFile.new_line("* recirculating shower")
mdFile.new_line("* heated floors")
mdFile.new_line("* elevated bed")
mdFile.new_line("* flares")

mdFile.new_header(level=2,title='Image:')
mdFile.new_line('![diagram](./images/vanbuild.jpg)')

mdFile.new_header(level=2,title='Current Promaster Estimates:')
mdFile.new_line("* total cost: "+str(total_cost))
mdFile.new_line("* total weight: "+str(total_weight))

print(str(build_items))
list_of_strings = ["Items", "Cost", "Weight"]
row_counter=1
for item in build_items:
    if item:
        print(item)
        print(str(build_items[item]))
        list_of_strings.extend([str(item),build_items[item]['cost'], build_items[item]['weight']])
        row_counter= row_counter+1

mdFile.new_line()
mdFile.new_table(columns=3, rows=row_counter, text=list_of_strings, text_align='center')



mdFile.create_md_file()


