const op = require('/MarkLogic/optic');

const quoteregex = /\"/g;

var schema
var table
var URI

uris = URI.split(";")

results = op.fromView(schema, table)
  .where(cts.documentQuery(uris))
  .map(row => {
    return Object.values(row)
      .map(cell => {
          var cell_string = String(cell)
          if(cell_string.includes("\"") || cell_string.includes("\n") || cell_string.includes(",")) {
            return "\"" + cell_string.replace(quoteregex, "\"\"") + "\""
          } else {
            return cell_string
          }
        }
      )
      .join(",")
  })
  .result()

Sequence.from(Array.from(results))
