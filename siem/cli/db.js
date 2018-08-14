const MongoClient = require('mongodb').MongoClient
const url = "mongodb://siem:siem@localhost:27017/siem"

// exporting default db client and url
module.exports = {
    url: url,
    MongoClient: MongoClient
}