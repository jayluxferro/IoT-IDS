var csv = require('fast-csv')

csv
      .fromPath('/root/dev/IoT-IDS/siem/logs/aps-01.csv')
      .on('data',  (data) => {
        //await sails.log(data)
	     console.log(data)
      })
      .on('end', () => {
        //sails.log('Done reading data file')
      })
      .on('error', () => {
        //sails.log('Error encountered')
      })
      .on('close', () => {
        //sails.log('Data file closed')
      })
