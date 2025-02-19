import sys

from lxml import etree


if __name__ == '__main__':
    assert len(sys.argv) == 2
    xml_schema_filepath = sys.argv[1]
    with open(xml_schema_filepath, 'rb') as xml_file:
        schema_root = etree.XML(xml_file.read())
    xml_schema = etree.XMLSchema(schema_root)
