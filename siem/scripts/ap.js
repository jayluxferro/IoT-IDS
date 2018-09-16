//{'group_cipher': 'CCMP', 'protocol': 'bgn', 'bssid': '50:2B:73:E4:4E:80', 'quality': '28', 'encryption_key': 'on', 'pairwise_ciphers': 'CCMP', 'frequency': '2.462', 'rsn_ie': '30140100000fac040100000fac040100000fac020c00', 'essid': '"sperixlabs"', 'bit_rates': '144', 'fm': '0003', 'signal_level': '-48', 'ie': 'IEEE 802.11i/WPA2 Version 1', 'authentication_suites': 'PSK', 'channel': '11', 'mode': 'Master'}
module.exports = {


  friendlyName: 'Ap',


  description: 'Default Access Point.',


  inputs: {

  },


  fn: async function (inputs, exits) {

    sails.log('Running custom shell script... (`ap`)');
    

    // calculating entropy
    /**
     * @param
     * group_cipher, protocol, bssid, encryption_key, pairwise_ciphers, frequency, rsn_ie, essid, bit_rates, fm, ie, authentication_suties, channel, mode 
     */
    

    data = {'group_cipher': 'CCMP', 'protocol': 'bgn', 'bssid': '50:2B:73:E4:4E:80', 'quality': '28', 'encryption_key': 'on', 'pairwise_ciphers': 'CCMP', 'frequency': '2.462', 'rsn_ie': '30140100000fac040100000fac040100000fac020c00', 'essid': '"sperixlabs"', 'bit_rates': '144', 'fm': '0003', 'signal_level': '-48', 'ie': 'IEEE 802.11i/WPA2 Version 1', 'authentication_suites': 'PSK', 'channel': '11', 'mode': 'Master', 'entropy': (-Math.log2(1/14))}

    var result = await Ap.create(data).intercept(err => {
      console.log(err)
    }).fetch()
    if(!result){
      console.log('Process failed')
      return exits.success()
    }
    console.log(result)
    // All done.
    return exits.success();

  }


};

