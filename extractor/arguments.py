import argparse
import sys

def parse() :
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    build_global_arguments(parser)
    build_subparsers(parser)

    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)

    return parser.parse_args()

def build_global_arguments(parser) :
    return

def build_subparsers(parser) :
    subparsers = parser.add_subparsers(required='true')

    build_extract_subparser(subparsers)

def build_extract_subparser(subparsers) :
    extract_parser = subparsers.add_parser("extract", formatter_class=argparse.ArgumentDefaultsHelpFormatter, argument_default=argparse.SUPPRESS)

    build_global_extract_arguments(extract_parser)

    build_schema_based_extract_arguments(extract_parser)
    build_config_based_extract_arguments(extract_parser)

def build_global_extract_arguments(extract_parser) :
    # Flags
    extract_parser.add_argument('-n', '--no-header', action='store_true', help='don\'t include a header line in exported files')
    extract_parser.add_argument('-c', '--count', action='store_true', help='create a count file for each exported file')

    # Options
    extract_parser.add_argument('--data-directory', action='store', default='./data/', help='the directory to store the extracted CSV files in')

def build_schema_based_extract_arguments(extract_parser) :
    extract_schema_parser = extract_parser.add_argument_group(title='schema based extract')

    # The schema to extract tables from
    extract_schema_parser.add_argument('--schema', action='store', help='the schema to extract')

    # Table filtering options (only 1 of them allowed at a time)
    extract_schema_table_group = extract_schema_parser.add_mutually_exclusive_group()

    extract_schema_table_group.add_argument('--include-tables', nargs='+', metavar='TABLE', action='store', help='a table to include in the extract, only used with SCHEMA')
    extract_schema_table_group.add_argument('--exclude-tables', nargs='+', metavar='TABLE', action='store', help='a table to exclude from the extract, only used with SCHEMA')
    extract_schema_table_group.add_argument('--table-filter', action='store', help='a filter to include/exclude tables in the extract')

    # Document filtering options
    extract_schema_parser.add_argument('--include-collections', nargs='+', metavar='COLLECTION', action='store', help='a collection to include data from in the extract, only used with SCHEMA')
    extract_schema_parser.add_argument('--exclude-coillections', nargs='+', metavar='COLLECTION', action='store', help='a collection to exclude data from extract, only used with SCHEMA')
    extract_schema_parser.add_argument('--document-filter', action='store', help='a filter to include/exclude documents in the extract')

def build_config_based_extract_arguments(extract_parser) :
    return
