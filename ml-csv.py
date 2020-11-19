#! python

import ml_csv.arguments
from  ml_csv.extract.command import execute as extract

arguments = ml_csv.arguments.parse_arguments()

print(arguments)

commands = {
    'extract': extract
}

commands[arguments.command](arguments)
