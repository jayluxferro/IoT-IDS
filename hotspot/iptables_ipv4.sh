sudo iptables -t nat -A POSTROUTING -o wlan2 -j MASQUERADE
sudo iptables -A FORWARD -i wlan2 -o wlan1 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan1 -o wlan2 -j ACCEPT
