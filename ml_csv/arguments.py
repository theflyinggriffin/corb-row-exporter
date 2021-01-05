import sys
import argparse
import ml_csv.extract.arguments as extract_arguments

def parse_arguments() :
    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)

    return build_argument_parser().parse_args()

def build_argument_parser() :
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers(title='command', dest='command', required='true', help='the comand to execute')

    extract_arguments.add_subparser(subparsers)

    return parser
