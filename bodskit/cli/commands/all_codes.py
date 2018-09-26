
from .base import BaseCommand

import bodskit.all_codes


class Command(BaseCommand):
    name = 'all-codes'
    help = 'generates a spreadsheet with all codelist items'

    def add_arguments(self):
        self.add_argument('codelist_directory', help='Directory that contains the code lists')

    def handle(self):
        all_codes = bodskit.all_codes.AllCodes(codelist_directory=self.args.codelist_directory)
        all_codes.handle()
