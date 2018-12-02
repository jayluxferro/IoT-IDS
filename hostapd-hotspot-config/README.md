# Hotspot Configuration of a Raspberry-Pi

## Install required packages
Run __install.sh__

## Deny wireless interface
1. Run __sudo nano /etc/dhcpcd.conf__
2. Paste __denyinterfaces wlan0__ at the bottom, where __wlan0__ is the wireless network interface
3. Save by pressing __Ctrl + O__
4. Exit by pressing __Ctrl + X__

## Edit Network configuration file
1. Run __sudo nano /etc/network/interfaces__
2. Clear the inital configuration for your wireless interface
3. Paste the contents of "__wlanConfig__"
4. Run "__sudo ifdown wlan0; sudo ifup wlan0__"

## Edit Hostapd configuration
1. Run "__sudo nano /etc/hostapd/hostapd.conf__"
2. Paste the contents of hostapd.conf

## Add default configuration hostapd daemon file
1. Run "__sudo nano /etc/default/hostapd__"
2. Find the line __#DAEMON_CONF=""__
3. Replace it with  __DAEMON_CONF="/etc/hostapd/hostapd.conf"__

## Create dnsmasq dhcp configuration file
1. Run "__sudo nano /etc/dnsmasq.conf__"
2. Replace all its contents with the contents of "**dnsmasq.conf**"

## Enable ipv4 forwarding
1. Run "__sudo nano /etc/sysctl.conf__"
2. Remove "#" from the beginning of the line containing __net.ipv4.ip_foward=1__

## Creating nat routing rule using iptables
1. Run "__iptables_ipv4.sh__"
2. Save the iptables rule by running: __sudo sh -c "iptables-save > /etc/iptables.ipv4.nat__"
3. Run "__sudo nano /etc/rc.local__"
4. Type the following line just before the "exit 0" line
     __iptables-restore < /etc/iptables.ipv4.nat__

## Starting services upon reboot
Run the following line:
    __sudo update-rc.d -f hostapd enable &&  sudo update-rc.d -f dnsmasq enable &&  sudo reboot__

Source: https://frillip.com/using-your-raspberry-pi-3-as-a-wifi-access-point-with-hostapd/
