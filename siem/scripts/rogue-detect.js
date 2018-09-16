module.exports = {


  friendlyName: 'Rogue detect',


  description: '',


  inputs: {

  },


  fn: async function (inputs, exits) {

    sails.log('Running custom shell script... (`rogue-detect`)');

    // All done.
    return exits.success();

  }


};

