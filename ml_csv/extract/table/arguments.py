
import argparse

def add_subparser(parser) :
    table_parser = parser.add_parser("table", help='extract CSV file for a single table', formatter_class=argparse.ArgumentDefaultsHelpFormatter, argument_default=argparse.SUPPRESS)

    table_parser.add_argument('schema', metavar='SCHEMA', help='the schema to extract from')
    table_parser.add_argument('table', metavar='TABLE', help='the table to extract')

    # Document filtering options
    document_group = table_parser.add_argument_group(title='Document Management', description='Filter documents to include in the qurery using collections or CTS queries')

    document_group.add_argument('--include-collections', nargs='+', metavar='COLLECTION', action='store', help='a collection to include data from in the extract')
    document_group.add_argument('--exclude-collections', nargs='+', metavar='COLLECTION', action='store', help='a collection to exclude data from extract')
    #document_group.add_argument('--document-filter', action='store', help='a filter to include/exclude documents in the extract')

    # corb  options
    corb_group = table_parser.add_argument_group(title='Corb Management', description='Change the default behavior of CORB2')

    corb_group.add_argument('--corb-options', action='store', default='./extract.options', help='the file containing the CORB2 options')
    #corb_group.add_argument('--batch-size', action='store', type=int, help='override the batch size defined in the CORB2 options file')
    #corb_group.add_argument('--thread-count', action='store', type=int, help='override the thread count defined in the CORB2 options file')

    # CSV file options
    csv_group = table_parser.add_argument_group(title='CSV Management', description='Change the default behavior of the CSV files')

    csv_group.add_argument('--data-directory', action='store', default='./data/', help='the directory to store the extracted CSV files in')
    #csv_group.add_argument('-n', '--no-header', action='store_true', help='don\'t include a header line in exported files')
