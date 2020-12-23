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
          if(cell.includes("\"") || cell.includes("\n") || cell.includes(",")) {
            return "\"" + cell.replace(quoteregex, "\"\"") + "\""
          } else {
            return cell
          }
        }
      )
      .join(",")
  })
  .result()

Sequence.from(Array.from(results))
