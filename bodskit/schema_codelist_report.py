import json
import csv
import sys
import pathlib
import os
from jsonref import JsonRef


class SchemaCodeListReport:

    def __init__(self, input_filename):
        self.input_filename = input_filename

    def _recurse(self, data, codelists):
        if isinstance(data, list):
            for item in data:
                self._recurse(item, codelists)
        elif isinstance(data, dict):
            if 'codelist' in data:
                codelist = data['codelist']
                if codelist not in codelists:
                    codelists[codelist] = {'open': False, 'closed': False}
                if 'openCodelist' in data and data['openCodelist']:
                    codelists[codelist]['open'] = True
                else:
                    codelists[codelist]['closed'] = True
            else:
                for value in data.values():
                    self._recurse(value, codelists)

    def handle(self):

        with open(self.input_filename) as fp:
            schema = json.load(fp)

        schema = JsonRef.replace_refs(schema, base_uri=pathlib.Path(os.path.realpath(self.input_filename)).as_uri())

        codelists = {}

        self._recurse(schema, codelists)

        out = []
        for codelist, codelist_data in sorted(codelists.items()):
            if codelist_data['open'] and codelist_data['closed']:
                type = 'Open AND Closed'
            elif codelist_data['open']:
                type = 'Open'
            else:
                type = 'Closed'
            out.append({
                'codelist': codelist,
                'type': type
            })

        w = csv.DictWriter(sys.stdout, ['codelist', 'type'])
        w.writeheader()
        w.writerows(out)
