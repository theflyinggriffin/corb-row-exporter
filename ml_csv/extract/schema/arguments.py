
import argparse

def add_subparser(parser) :
    schema_parser = parser.add_parser("schema", help='extract CSV files for tables from a specific schema', formatter_class=argparse.ArgumentDefaultsHelpFormatter, argument_default=argparse.SUPPRESS)

    schema_parser.add_argument('schema', metavar='SCHEMA', help='the schema to extract tables from')

    # Table filtering options (only 1 of them allowed at a time)
    table_group = schema_parser.add_argument_group(title='Table Management', description='Filter tables to include in the extract')
    table_mux_group = table_group.add_mutually_exclusive_group()

    table_mux_group.add_argument('--include-tables', nargs='+', metavar='TABLE', action='store', help='a table to include in the extract, only used with SCHEMA')
    table_mux_group.add_argument('--exclude-tables', nargs='+', metavar='TABLE', action='store', help='a table to exclude from the extract, only used with SCHEMA')
    table_mux_group.add_argument('--table-filter', action='store', help='a filter to include/exclude tables in the extract')

    # Document filtering options
    document_group = schema_parser.add_argument_group(title='Document Management', description='Filter documents to include in the qurery using collections or CTS queries')

    document_group.add_argument('--include-collections', nargs='+', metavar='COLLECTION', action='store', help='a collection to include data from in the extract, only used with SCHEMA')
    document_group.add_argument('--exclude-collections', nargs='+', metavar='COLLECTION', action='store', help='a collection to exclude data from extract, only used with SCHEMA')
    #document_group.add_argument('--document-filter', action='store', help='a filter to include/exclude documents in the extract')

    # corb  options
    corb_group = schema_parser.add_argument_group(title='Corb Management', description='Change the default behavior of CORB2')

    corb_group.add_argument('--corb-options', action='store', default='./extract.options', help='the file containing the CORB2 options')
    #corb_group.add_argument('--batch-size', action='store', type=int, help='override the batch size defined in the CORB2 options file')
    #corb_group.add_argument('--thread-count', action='store', type=int, help='override the thread count defined in the CORB2 options file')

    # CSV file options
    csv_group = schema_parser.add_argument_group(title='CSV Management', description='Change the default behavior of the CSV files')

    csv_group.add_argument('--data-directory', action='store', default='./data/', help='the directory to store the extracted CSV files in')
    #csv_group.add_argument('-n', '--no-header', action='store_true', help='don\'t include a header line in exported files')
