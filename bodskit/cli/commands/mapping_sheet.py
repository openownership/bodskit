
from .base import BaseCommand

import bodskit.mapping_sheet


class Command(BaseCommand):
    name = 'mapping-sheet'
    help = 'generates a spreadsheet with all field paths from an BODS schema'

    def add_arguments(self):
        self.add_argument('schema_file', help='schema_file')

    def handle(self):

        mapping_sheet = bodskit.mapping_sheet.MappingSheet(input_filename=self.args.schema_file)
        mapping_sheet.handle()
