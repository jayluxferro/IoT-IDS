var csv = require('fast-csv')
module.exports = {
  friendlyName: 'APS',
  description: 'Display all access points data',
  inputs: {

  },
  fn: async function (inputs, exits) {
    var log_file = require('path').resolve(sails.config.appPath, 'logs/aps-01.csv')

     var response = await csv.fromPath(log_file)
     //sails.log(response)
     await response.on('data', async (data) => {
        await console.log(data)
     })
     /*
      .fromPath (log_file)
      .on('data', (data) => {
         sails.log(data)
      })
      .on('end', () => {
        sails.log('Done reading data file')
      })
      .on('error', () => {
        sails.log('Error encountered')
      })
      .on('close', () => {
        sails.log('Data file closed')
      })
      */

    // All done.
    return exits.success()

  }
}

