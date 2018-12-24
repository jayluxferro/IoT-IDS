#!/usr/bin/python

"""
Address Resolution Protocol parser
Author: Jay Lux Ferro
Date: 24th Dec 2018 
"""

import sys
import subprocess

def usage():
    print('Usage: python ' + sys.argv[0] + ' [network interface]')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    

    # getting arp information
    result =  subprocess.check_output(['arp', '-a'], shell=False).split('\n')
    arp_data = []
    for x in result:
        fields = x.split(' ')
        if len(fields) is not 7:
            continue
        ip_address = fields[1].strip('()')
        mac_address = fields[3]
        interface = fields[6]
        gateway = True if fields[0] == '_gateway' else False
        if interface == sys.argv[1]:
            arp_data.append({'ip': ip_address, 'mac': mac_address, 'interface': interface, 'gateway': gateway})

    print(arp_data)
        
     
