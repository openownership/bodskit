import os
from io import StringIO
from unittest.mock import patch
import bodskit.schema_codelist_report


def test_command():

    input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  '..', 'fixtures', 'test-schema-codelist-report.json')

    with patch('sys.stdout', new_callable=StringIO) as actual:

        schema_codelist_report = bodskit.schema_codelist_report.SchemaCodeListReport(input_filename=input_filename)
        schema_codelist_report.handle()

    assert actual.getvalue().replace("\r", "") == '''codelist,type
a.csv,Open AND Closed
b.csv,Open
c.csv,Closed
d.csv,Closed
'''


def test_schema():

    input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  '..', 'fixtures', 'schema', 'bods-package.json')

    with patch('sys.stdout', new_callable=StringIO) as actual:

        schema_codelist_report = bodskit.schema_codelist_report.SchemaCodeListReport(input_filename=input_filename)
        schema_codelist_report.handle()

    assert actual.getvalue().replace("\r", "") == '''codelist,type
addressType.csv,Closed
annotationMotivation.csv,Open
entityType.csv,Closed
interestLevel.csv,Closed
interestType.csv,Closed
nameType.csv,Closed
personType.csv,Closed
sourceType.csv,Closed
statementType.csv,Closed
unspecifiedReason.csv,Closed
'''
