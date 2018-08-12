module.exports = {
    friendlyName: 'Dashboard',
    description: 'Main Dashboard',
    fn: async function(){
        return this.res.view('pages/dashboard')
    }
}