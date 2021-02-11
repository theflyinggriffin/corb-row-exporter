import os
import platform
import subprocess
import sys
import ml_csv.extract.corb_resources.table_extract as corb_base

classpath_separator = ";" if platform.system() == "Windows" else ":"

corbCommandStart = ['java',
                    '-server',
                    '-cp',
                    classpath_separator.join(['.', 'marklogic-xcc-10.0.5.jar', 'marklogic-corb-2.4.6.jar'])
                   ]

corbCommandEnd = ['com.marklogic.developer.corb.Manager']

corb_base_path = os.path.abspath(os.path.dirname(corb_base.__file__))

init_module = os.path.join(corb_base_path, 'header.js')
uris_module = os.path.join(corb_base_path, 'uris.js')
process_module = os.path.join(corb_base_path, 'rows.js')

def extract(schema, table, arguments) :
    options = []

    options.append('-DOPTIONS-FILE=' + arguments.corb_options)

    # INIT module options
    options.append("-DINIT-MODULE=" + init_module + "|ADHOC")
    options.append("-DINIT-TASK=com.marklogic.developer.corb.ExportBatchToFileTask")
    options.append("-DINIT-MODULE.schema=" + schema)
    options.append("-DINIT-MODULE.table=" + table)

    # URI module options
    options.append("-DURIS-MODULE=" + uris_module + "|ADHOC")
    options.append("-DURIS-MODULE.schema=" + schema)
    options.append("-DURIS-MODULE.table=" + table)

    # Process module options
    options.append("-DPROCESS-MODULE=" + process_module + "|ADHOC")
    options.append("-DPROCESS-TASK=com.marklogic.developer.corb.ExportBatchToFileTask")
    options.append("-DPROCESS-MODULE.schema=" + schema)
    options.append("-DPROCESS-MODULE.table=" + table)

    # OTHER options
    options.append("-DEXPORT-FILE-NAME=" + os.path.join(arguments.data_directory, schema, table + ".csv"))

    if "include_collections" in arguments :
        options.append("-DURIS-MODULE.includeCollections=" + ','.join(arguments.include_collections))


    if "exclude_collections" in arguments :
        options.append("-DURIS-MODULE.excludeCollections=" + ','.join(arguments.exclude_collections))

    command = corbCommandStart + options + corbCommandEnd
    #print(command)
    subprocess.call(command)
