import os
from io import StringIO
from unittest.mock import patch
import bodskit.schema_report


def test_command():

    input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  '..', 'fixtures', 'test-schema-report.json')

    with patch('sys.stdout', new_callable=StringIO) as actual:

        schema_report = bodskit.schema_report.SchemaReport(input_filename=input_filename)
        schema_report.handle()

    assert actual.getvalue() == '''openCodelist: False
a.csv
b.csv
c.csv
d.csv

'''
