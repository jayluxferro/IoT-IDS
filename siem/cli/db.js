var MongoClient = require('mongodb').MongoClient
var url = "mongodb://siem:siem@localhost:27017/siem"

MongoClient.connect(url, { useNewUrlParser: true }, function(err, db) {
    if (err) throw err
    console.log("Database connected!")
    db.close()
})