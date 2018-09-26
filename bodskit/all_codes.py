import glob
import csv
import os
import sys


class AllCodes:

    def __init__(self, codelist_directory):
        self.codelist_directory = codelist_directory

    def handle(self):

        data = []

        for path in glob.glob(os.path.join(self.codelist_directory, '*.csv')):
            with open(path) as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=['code', 'title', 'description', 'technical note'])
                next(reader, None)  # skip the headers
                for row in reader:
                    row['codelist'] = os.path.splitext(os.path.basename(path))[0]
                    data.append(row)

        w = csv.DictWriter(sys.stdout, ['codelist', 'code', 'title', 'description', 'technical note'])
        w.writeheader()
        w.writerows(data)
