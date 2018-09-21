import json


class SchemaReport:

    def __init__(self, input_filename):
        self.input_filename = input_filename

    def handle(self):
        def recurse(data, codelists):
            if isinstance(data, list):
                for item in data:
                    recurse(item, codelists)
            elif isinstance(data, dict):
                if 'codelist' in data:
                    codelist = data['codelist']
                    # If the CSV file is used for open and closed codelists, treat it as closed.
                    if codelist not in codelists:
                        codelists[codelist] = data['openCodelist']
                    elif not data['openCodelist']:
                        codelists[codelist] = data['openCodelist']
                else:
                    for value in data.values():
                        recurse(value, codelists)

        with open(self.input_filename) as fp:
            schema = json.load(fp)

        codelists = {}
        recurse(schema, codelists)

        partitioned_codelists = {
            True: set(),
            False: set(),
        }

        for codelist, open_codelist in codelists.items():
            partitioned_codelists[open_codelist].add(codelist)

        for open_codelist, codelists in partitioned_codelists.items():
            if codelists:
                print('openCodelist: {}\n{}\n'.format(open_codelist, '\n'.join(sorted(codelists))))
