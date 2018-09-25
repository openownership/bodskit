import os
from io import StringIO
from unittest.mock import patch

from tests import read_fixture

import bodskit.all_codes


def test_command():

    codelist_directory = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), '..', 'fixtures', 'schema', 'codelists'
    )

    with patch('sys.stdout', new_callable=StringIO) as actual:
        all_codes = bodskit.all_codes.AllCodes(codelist_directory=codelist_directory)
        all_codes.handle()

    assert actual.getvalue() == \
        read_fixture('all-codes.csv').replace('\n', '\r\n')  # not sure why
