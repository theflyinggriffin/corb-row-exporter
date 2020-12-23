const op = require('/MarkLogic/optic');

var schema
var table

results = op.fromView(schema, table)
  .select(null, "")
  .limit(1)
  .map(row => {
    return Object.keys(row).join(",")
  })
  .result()

Sequence.from(Array.from(results))
