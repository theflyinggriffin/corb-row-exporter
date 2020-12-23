const op = require('/MarkLogic/optic');

var schema
var table

var includeCollections
var excludeCollections

filters = []

if(includeCollections && includeCollections.length > 0) {
  filters.push(cts.collectionQuery(includeCollections.split(',')))
}

if(excludeCollections && excludeCollections.length > 0) {
  filters.push(cts.notQuery(cts.collectionQuery(excludeCollections.split(','))))
}

documentFilterQuery = cts.andQuery(filters)

uris = op.fromView(schema, table, null, op.fragmentIdCol('docId'))
  .where(documentFilterQuery) //optional
  .joinDocUri('uri', op.fragmentIdCol('docId'))
  .select(['uri'])
  .whereDistinct()
  .result()
  .toArray()
  .map(result => {
    return result.uri
  });

length = uris.length

uris.unshift(length)

Sequence.from(uris)
