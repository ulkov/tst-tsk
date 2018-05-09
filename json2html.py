import json
from collections import OrderedDict
import xml.etree.ElementTree as ET


def _getParList():
    with open('source.json', 'rt', encoding='utf-8') as f:
        return json.loads(f.read(), object_pairs_hook=OrderedDict)


def _toHTML(parList):
    html = ET.Element('_')
    
    for el in parList:
        for k, v in el.items():
            html_el = ET.Element(k)
            html.append(html_el)
            html_el.text = v
    
    return ET.tostring(html, encoding="unicode", method="html")[3:][:-4] # remove '<_>' and '</_>'


def getHTML():
    try:
        parList = _getParList()
    except Exception as ex:
        return 'can not get paragraph list. error: %s' % ex
    
    try:
        html = _toHTML(parList)
    except Exception as ex:
        return 'can not render html. error: %s' % ex
    
    return html


if __name__ == '__main__':
    print(getHTML())