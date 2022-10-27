from argparse import ArgumentError

def build_xml_element(tag, content, **properties):
    if type(tag) != str or type(content) != str:
        raise ArgumentError("Please give valid inputs!")

    xml_element = "<" + tag
    for key in properties:
        xml_element += " " + key + "=\\\"" + properties[key] + "\\\""
    xml_element += "> " + content + "</" + tag + ">"

    return xml_element

print(build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))