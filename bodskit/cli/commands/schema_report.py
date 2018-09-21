from .base import BaseCommand
import bodskit.schema_report


class Command(BaseCommand):
    name = 'schema-report'
    help = 'reports details of a JSON Schema (open and closed codelists)'

    def add_arguments(self):
        self.add_argument('schema_file', help='schema_file')

    def handle(self):
        schema_report = bodskit.schema_report.SchemaReport(input_filename=self.args.schema_file)
        schema_report.handle()
