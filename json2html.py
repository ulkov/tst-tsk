import json
import xml.etree.ElementTree as ET


def _getParList():
    with open('source.json', 'rt', encoding='utf-8') as f:
        return json.loads(f.read())


def _toHTML(parList):
    html = ET.Element('_')
    
    for el in parList:
        h1 = ET.Element('h1')
        html.append(h1)
        h1.text = el['title']
        
        p = ET.Element('p')
        html.append(p)
        p.text = el['body']
        
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