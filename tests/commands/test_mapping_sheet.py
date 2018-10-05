import os
from io import StringIO
from unittest.mock import patch

from tests import read_fixture

import bodskit.mapping_sheet


def test_command():

    input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  '..', 'fixtures', 'schema', 'person-statement.json')

    with patch('sys.stdout', new_callable=StringIO) as actual:
        mapping_sheet = bodskit.mapping_sheet.MappingSheet(input_filename=input_filename)
        mapping_sheet.handle()

    assert actual.getvalue() == \
        read_fixture('mapping-sheet-person-statement.csv').replace('\n', '\r\n')  # not sure why


def test_enum_in_list():
    """Special test for problem reported with sourceType checklist - values where not being reported"""

    input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  '..', 'fixtures', 'mapping-sheet-enum-in-list-input.json')

    with patch('sys.stdout', new_callable=StringIO) as actual:
        mapping_sheet = bodskit.mapping_sheet.MappingSheet(input_filename=input_filename)
        mapping_sheet.handle()

    assert actual.getvalue() == \
        read_fixture('mapping-sheet-enum-in-list-output.csv').replace('\n', '\r\n')  # not sure why


def test_codelist():

    input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  '..', 'fixtures', 'mapping-sheet-codelist-input.json')

    with patch('sys.stdout', new_callable=StringIO) as actual:
        mapping_sheet = bodskit.mapping_sheet.MappingSheet(input_filename=input_filename)
        mapping_sheet.handle()

    assert actual.getvalue() == \
        read_fixture('mapping-sheet-codelist-output.csv').replace('\n', '\r\n')  # not sure why
