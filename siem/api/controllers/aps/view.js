module.exports = {
    friendlyName: 'Access Points',
    inputs: {
        data: {
            type: 'string'
        }
    },
    exits: {
        success: {
            outputExample: {
                data: {}
            }
        },
    },
    fn: async function(inputs, exits){
        var result = new Array()
        await Aps.stream()
        .sort('power DESC')
        .eachRecord( async(d, next) => {
            if((new Date().getTime() - new Date(d.lastTimeSeen).getTime()) <= 10000)
                result.push(d)
            return next()
        })
        return exits.success({
            data: result
        })
    }
}