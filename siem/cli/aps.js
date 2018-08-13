var csv = require('fast-csv')
var path = require('path')
var log_path = path.resolve(__dirname, '../logs/aps-01.csv')
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
var terminate = false

csv
.fromPath(log_path)
.on('data', (data) => {
    if(data[0] !== undefined && data[0] !== 'BSSID'){
        if(data[0] === 'Station MAC'){
            terminate = true
        }
        
        if(!terminate){
            console.log(data)
        }
    }
})
.on('end', () => {

})