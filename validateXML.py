from lxml import etree
import sys as sys

source_file = sys.argv[1]
schema_file = sys.argv[2]

with open(schema_file) as f_schema:

    schema_doc = etree.parse(f_schema)
    schema = etree.XMLSchema(schema_doc)
    parser = etree.XMLParser(schema = schema)

    with open(source_file) as f_source:
        try:
            doc = etree.parse(f_source, parser)
            print ("XML file valid")
        except etree.XMLSyntaxError as e:
            # this exception is thrown on schema validation error
            print (e)
