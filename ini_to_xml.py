# -*- coding: UTF-8 -*-

import os
import xml.etree.cElementTree as ET
from xml.dom import minidom
from parse_ini_conf import fun_get_configuration



# 生成XML配置文件
def fun_generate_xml(v_file_path):
    file_name = os.path.basename(v_file_path)
    section = os.path.splitext(file_name)[0]

    site_tree = ET.parse(v_file_path)
    root_Element = site_tree.getroot()  # configuration

    # 删除配置
    for property in root_Element.findall('property'):
        root_Element.remove(property)

    # 添加配置
    list_configuration = fun_get_configuration(section)
    for tuple_property in list_configuration:
        property = ET.Element('property')
        name = ET.SubElement(property, 'name')
        name.text = tuple_property[0]
        value = ET.SubElement(property, 'value')
        value.text = tuple_property[1]
        root_Element.append(property)

    fun_indent(root_Element)
    site_tree.write(v_file_path, xml_declaration=True, encoding="utf-8", method="xml")



#输出带缩进格式的xml
def fun_indent( elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            fun_indent(e, level+1)
        if not e.tail or not e.tail.strip():
            e.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i
    return elem



if __name__ == '__main__':
    fun_generate_xml('E:/MyProjects/Python/generate-xml-conf/local_conf\core-site.xml')








