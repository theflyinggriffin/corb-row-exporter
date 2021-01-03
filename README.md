# MarkLogic CSV Extractor

## Introduction

The MarkLogic CSV Extractor is a wrapper around [Corb2](https://developer.marklogic.com/code/corb/) that will automate the discovery and extraction of tables built from TDEs.

## Installation

Prerequisites:
- Java 8 installed
- Python 3 installed

Get the code from this repository

```
git clone https://github.com/theflyinggriffin/ml-csv-extractor.git
cd ml-csv-extractor
```

Download the Corb2 and XCC jar files. The currently supported version are:

- Corb2 version [2.4.6](https://github.com/marklogic-community/corb2/releases/tag/v2.4.6)
- XCC version [10.0.5](https://developer.marklogic.com/download/binaries/10.0/MarkXCC.Java-10.0.5.zip)

## Usage

To extract data from `example.table1`, run the command:

```
python ml-csv.py extract table example table1
```

Or to extract all tables from the schema `example`, run the command:

```
python ml-csv.py extract schema example
```

For more options, use `-h` or `--help`, for example:

```
python ml-csv.py extract --help
```

or

```
python ml-csv.py extract table --help
```

## Limitations

The MarkLogic CSV Extractor currently only works on Linux based systems due to the difference in how Java expects the classpath parameter to be passed.
