#!/bin/bash

# installing packages
echo "Updating sources list"
sudo apt-get update

echo "Installing packages"
sudo apt-get install dnsmasq hostapd -y

echo "Configuring the interfaces"
sudo echo "denyinterfaces wlan0" >> /etc/dhcpcd.conf


