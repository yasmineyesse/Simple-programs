""" Read XML file """
# Created by Yenami
# Date : May 24, 2017

from lxml import etree

tree = etree.parse("file_xml.xml")

print("Text")
for t in tree.xpath("//t"):
    print(t.text)

print("Hypothesis")
for h in tree.xpath("//h"):
    print(h.text)