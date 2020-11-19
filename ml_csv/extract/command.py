
from .schema.method import execute as schema
from .table.method import execute as table

def execute(arguments) :
    print("the execute function of the extract command")

    commands = {
        'schema': schema,
        'table': table
    }

    commands[arguments.method](arguments)
