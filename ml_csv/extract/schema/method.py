import os
import subprocess
import csv
from .. import table_extractor
import ml_csv.extract.corb_resources.tables_to_extract as corb_base

corbCommandStart = ['java', '-Xmx80g', '-XX:+UseConcMarkSweepGC', '-server', '-cp', '.:marklogic-xcc-10.0.4.jar:marklogic-corb-2.4.6.jar']
csvExtractCommandStart = corbCommandStart + ['-DOPTIONS-FILE=configured-csv-extract/csv-extract.options']

corbCommandEnd = ['com.marklogic.developer.corb.Manager']

corb_base_path = os.path.abspath(os.path.dirname(corb_base.__file__))

uris_module = os.path.join(corb_base_path, 'uris.js')
process_module = os.path.join(corb_base_path, 'tables.js')

def execute(arguments) :
    schema = arguments.schema

    tables = get_tables_from_schema(schema, arguments)

    for table in tables :
        table_extractor.extract(schema, table, arguments)

def get_tables_from_schema(schema, arguments) :
    table_file = os.path.join(arguments.data_directory, 'tmp', 'tables.csv')


    if 'table_filter' in vars(arguments).keys() :
        table_filter = arguments.table_filter
    else :
        table_filter = None

    extract_table_list(schema, table_filter, arguments.corb_options, table_file)

    tables = []

    with open(table_file, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            tables.append(row[1])

    return tables

def extract_table_list(schema, table_filter, corb_options, table_file) :
    options = []

    options.append('-DOPTIONS-FILE=' + corb_options)
    options.append("-DEXPORT-FILE-NAME=" + table_file)

    options.append("-DURIS-MODULE=" + uris_module + "|ADHOC")

    options.append("-DPROCESS-MODULE=" + process_module + "|ADHOC")
    options.append("-DPROCESS-TASK=com.marklogic.developer.corb.ExportBatchToFileTask")
    options.append("-DPROCESS-MODULE.schema=" + schema)
    
    if table_filter is not None :
        options.append("-DPROCESS-MODULE.table_filter=" + table_filter)

    options.append('-DBATCH-SIZE=1')
    options.append('-DTHREAD-COUNT=1')

    command = corbCommandStart + options + corbCommandEnd
    #print(command)
    subprocess.call(command)

