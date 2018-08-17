var csv = require('fast-csv')
var path = require('path')
var log_path = path.resolve(__dirname, '../logs/aps-01.csv')
var db = require('./db')
var url = db.url
var MongoClient = db.MongoClient
/*
Data format to be received
[ 'BSSID',
  ' First time seen',
  ' Last time seen',
  ' channel',
  ' Speed',
  ' Privacy',
  ' Cipher',
  ' Authentication',
  ' Power',
  ' # beacons',
  ' # IV',
  ' LAN IP',
  ' ID-length',
  ' ESSID',
  ' Key' ]
*/

// clear previous data
try{
    MongoClient.connect(url, { useNewUrlParser: true }, (err, d )=>  {
        if (err) throw err
        var dbo = d.db("siem")
        dbo.collection("ap").drop((err, delOK) => {
          if (err) console.log(err)
          if (delOK) console.log("Collection deleted")
          d.close()
        })
    })
}catch(e){

}


var terminate = false
counter = 1
csv
.fromPath(log_path)
.on('data', (data) => {
    if(data[0] !== undefined && data[0] !== 'BSSID'){
        if(data[0] === 'Station MAC'){
            terminate = true
        }

        if(!terminate){
            // connect to database and add new dataset  
            //console.log(data)
            var dataset = {
                bssid: data[0].trim(),
                firstTimeSeen: data[1].trim(),
                lastTimeSeen: data[2].trim(),
                channel: data[3].trim(),
                speed: data[4].trim(),
                privacy: data[5].trim(),
                cipher: data[6].trim(),
                authentication: data[7].trim(),
                power: parseInt(data[8].trim()),
                beacons: data[9].trim(),
                iv: data[10].trim(),
                lanIP: data[11].trim(),
                idLength: data[12].trim(),
                essid: data[13].trim(),
                key: data[14] ? data[14].trim() : '',
                createdAt: new Date().getTime(),
                updatedAt: new Date().getTime(),
            }

            if(dataset.power !== '-1'){
                MongoClient.connect(url, { useNewUrlParser: true }, (err, conn) => {
                    if(err) throw err
                    var dbClient = conn.db('siem')
                    // adding dataset to db
                    dbClient.collection('ap').insertOne(dataset, (err, res) => {
                        if(err) throw err
                        counter++      
                    })
                    conn.close()
                }) 
            }
        }
    }
})
.on('end', () => {
    console.log('Data Migration Completed...')
})


/*
MongoClient.connect(url, { useNewUrlParser: true }, (err, conn) => {
    if(err) throw err
    console.log('Database connected..')
    var dbClient = conn.db('siem')
    console.log
    // retrieving data
    var counter = 1
    csv
    .fromPath(log_path)
    .on('data', (data) => {
        if(data[0] !== undefined && data[0] !== 'BSSID'){
            if(data[0] === 'Station MAC'){
                terminate = true
            }

            if(!terminate){
                // connect to database and add new dataset  
                console.log(data)
                var dataset = {
                    bssid: data[0].trim(),
                    firstTimeSeen: data[1].trim(),
                    lastTimeSeen: data[2].trim(),
                    channel: data[3].trim(),
                    speed: data[4].trim(),
                    privacy: data[5].trim(),
                    cipher: data[6].trim(),
                    authentication: data[7].trim(),
                    power: data[8].trim(),
                    beacons: data[9].trim(),
                    iv: data[10].trim(),
                    lanIP: data[11].trim(),
                    idLength: data[12].trim(),
                    essid: data[13].trim(),
                    key: data[14] ? data[14].trim() : ''
                }

                dbClient.collection('AP').insertOne(dataset, (err, res) => {
                    if(err) throw err
                    console.log('Data added: ' + str(counter))
                    counter++      
                })
            }
        }
    })
    .on('end', () => {

    })
    conn.close()
})

*/