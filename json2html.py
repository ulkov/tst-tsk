import json
from collections import OrderedDict
import xml.etree.ElementTree as ET
import re


def _getParList(fname):
    with open(fname, 'rt', encoding='utf-8') as f:
        return json.loads(f.read(), object_pairs_hook=OrderedDict)


def _toHTML(parList):
    html = ET.Element('_')
    
    def renderObj(obj, parentEl):
        if isinstance(obj, list):
            ul = ET.Element('ul')
            parentEl.append(ul)
            for el in obj:
                li = ET.Element('li')
                ul.append(li)
                renderObj(el, li)
        else:
            for k, v in obj.items():
                html_el = _createEl(k)
                parentEl.append(html_el)
                if isinstance(v, list):
                    renderObj(v, html_el)
                else:
                    html_el.text = v
    
    renderObj(parList, html)
    
    return ET.tostring(html, encoding="unicode", method="html")[3:][:-4] # remove '<_>' and '</_>'


def _createEl(src):
    attrib = {}
    cls = []
    for a in re.findall('[\#\.][_a-zA-Z0-9-]*', src):
        if a.startswith('.'):
            cls.append(a[1:])
        elif a.startswith('#'):
            attrib['id'] = a[1:]
    if cls:
        attrib['class'] = ' '.join(cls)
    
    tag = re.split('[\#\.]', src)[0]
    
    return ET.Element(tag, attrib=attrib)



def getHTML(fname='source.json'):
    try:
        parList = _getParList(fname)
    except Exception as ex:
        return 'can not get paragraph list. error: %s' % ex
    
    try:
        html = _toHTML(parList)
    except Exception as ex:
        return 'can not render html. error: %s' % ex
    
    return html


if __name__ == '__main__':
    print(getHTML())
    print(getHTML('source2.json'))
    print(getHTML('source3.json'))