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
