import argparse
import importlib
import json
import logging.config
import sys

from bodskit.exceptions import CommandError

logger = logging.getLogger('bodskit')

COMMAND_MODULES = (
    'bodskit.cli.commands.mapping_sheet',
    'bodskit.cli.commands.schema_codelist_report',
    'bodskit.cli.commands.all_codes',
)


def main():
    parser = argparse.ArgumentParser(description='BODSKit CLI')

    subparsers = parser.add_subparsers(dest='subcommand')

    subcommands = {}

    for module in COMMAND_MODULES:
        try:
            command = importlib.import_module(module).Command(subparsers)
            subcommands[command.name] = command
        except ImportError as e:
            logger.error('exception "%s" prevented loading of %s module', e, module)

    args = parser.parse_args()

    if args.subcommand:
        command = subcommands[args.subcommand]
        try:
            command.args = args
            try:
                command.handle()
            except json.decoder.JSONDecodeError as e:
                raise CommandError('JSON error: {}\nIs the JSON data not line-delimited? '
                                   'Try piping it through `jq -crM .`'.format(e))
        except CommandError as e:
            logger.critical(e)
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
