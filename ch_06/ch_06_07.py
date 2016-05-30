from xml.etree.ElementTree import parse

doc = parse('07.xml')

print doc.findtext(
    'content/{http://www.w3.org/1999/xhtml}html/{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title')
