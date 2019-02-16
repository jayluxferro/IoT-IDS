const MongoClient = require('mongodb').MongoClient
const url = "mongodb://@localhost:27017/siem"

// exporting default db client and url
module.exports = {
    url: url,
    MongoClient: MongoClient
}
