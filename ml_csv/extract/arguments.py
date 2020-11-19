
import argparse
import ml_csv.extract.schema.arguments as schema_arguments
import ml_csv.extract.table.arguments as table_arguments
#import table.arguments

def add_subparser(parser) :
    extract_parser = parser.add_parser("extract", help='extract CSV files', formatter_class=argparse.ArgumentDefaultsHelpFormatter, argument_default=argparse.SUPPRESS)

    subparsers = extract_parser.add_subparsers(title='method', dest='method', required='true', help='the method used to extract CSV files')

    table_arguments.add_subparser(subparsers)
    schema_arguments.add_subparser(subparsers)
