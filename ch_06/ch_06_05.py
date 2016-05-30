from xml.etree.ElementTree import Element, tostring


def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)

print e
print tostring(e)

e.set('_id', '1234')

print tostring(e)


def dict_to_xml_str(tag, d):

    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key,val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)

print dict_to_xml_str('stock', s)

from xml.sax.saxutils import escape, unescape

print escape('<spam>')
