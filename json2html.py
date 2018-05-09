import json
from collections import OrderedDict
import xml.etree.ElementTree as ET


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
                html_el = ET.Element(k)
                parentEl.append(html_el)
                if isinstance(v, list):
                    renderObj(v, html_el)
                else:
                    html_el.text = v
    
    renderObj(parList, html)
    
    return ET.tostring(html, encoding="unicode", method="html")[3:][:-4] # remove '<_>' and '</_>'


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