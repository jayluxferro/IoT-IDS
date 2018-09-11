// BSSID	 First time seen	 Last time seen	 channel	 Speed	 Privacy	 Cipher	 Authentication	 Power	 # beacons	 # IV	 LAN IP	 ID-length	 ESSID	 Key

module.exports = {
    attributes: {
        bssid: {
            type: 'string',
            required: true
        },
        firstTimeSeen: {
            type: 'string',
            required: true
        },
        lastTimeSeen: {
            type: 'string',
            required: true
        },
        channel: {
            type: 'string',
            required: true
        },
        speed: { 
            type: 'string',
            required: true
        },
        privacy: {
            type: 'string',
            required: true // eg. WPA2 WPA
        },
        cipher: {
            type: 'string'
        },
        authentication: {
            type: 'string'
        },
        power: {
            type: 'number',
            required: true
        },
        beacons: {
            type: 'string',
            required: true
        },
        iv: {
            type: 'string',
            required: true
        },
        lanIP: {
            type: 'string',
            required: true
        },
        idLength: {
            type: 'string',
            required: true
        },
        essid: {
            type: 'string'
        },
        key: {
            type: 'string'
        }
    }
}