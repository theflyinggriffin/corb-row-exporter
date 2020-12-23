const op = require('/MarkLogic/optic');

var URI;

var schema
var table_filter

const quoteregex = /\"/g;

var opticplan = op.fromView("sys", "sys_tables")
  .where(op.eq(op.col("schema"), schema))

if(table_filter && table_filter.length > 0) {
  opticplan = opticplan.where(op.sqlCondition(table_filter))
}

var results = opticplan.select(['schema', 'name'])
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
