
from .. import table_extractor

def execute(arguments) :
    print("the execute function of the table method")

    table_extractor.extract(arguments.schema, arguments.table, arguments)
