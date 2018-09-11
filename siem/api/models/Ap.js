//{'group_cipher': 'CCMP', 'protocol': 'bgn', 'bssid': '50:2B:73:E4:4E:80', 'quality': '1', 'encryption_key': 'on', 'pairwise_ciphers': 'CCMP', 'frequency': '2.437', 'rsn_ie': '30140100000fac040100000fac040100000fac020c00', 'essid': '"sperixlabs"', 'bit_rates': '144', 'fm': '0003', 'signal_level': '-99', 'ie': 'IEEE 802.11i/WPA2 Version 1', 'authentication_suites': 'PSK', 'channel': '6', 'mode': 'Master'}
module.exports = {
    attributes: {
        group_cipher: {
            type: 'string',
        },
        protocol: {
            type: 'string',
        },
        bssid: {
            type: 'string',
        },
        quality: {
            type: 'string',
        },
        encryption_key: { 
            type: 'string',
        },
        pairwise_ciphers: {
            type: 'string',
        },
        frequency: {
            type: 'string'
        },
        rsn_ie: {
            type: 'string'
        },
        essid: {
            type: 'number',
        },
        bit_rates: {
            type: 'string',
        },
        fm: {
            type: 'string',
        },
        signal_level: {
            type: 'string',
        },
        ie: {
            type: 'string',
        },
        authentication_suites: {
            type: 'string'
        },
        channel: {
            type: 'string'
        },
        mode: {
            type: 'string'
        }
    }
}