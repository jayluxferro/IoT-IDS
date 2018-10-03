#!/usr/bin/python

from scapy.all import *
import pymongo
import pprint
import os
import psutil

# init
dbClient = pymongo.MongoClient("mongodb://siem:siem@localhost:27017/siem")
db = dbClient["siem"]
ap = db["ap"]
single = db["single"]
device = ap.find({}).limit(1)
xtics = None
for x in device:
  xtics = x
#print(xtics)


def get_usage():
  pid = os.getpid()
  py = psutil.Process(pid)
  #print(py.memory_percent())
  #print(py.cpu_percent())
  return py.memory_percent()


def hex_to_ascii(h):
    chars_in_reverse = []
    while h != 0x0:
        chars_in_reverse.append(chr(h & 0xFF))
        h = h >> 8

    chars_in_reverse.reverse()
    return ''.join(chars_in_reverse)


def get_channel(channel):
  return int(pprint.pformat(channel).split('\\x')[1].split("'")[0], 16)


def packetHandler(pkt):
  if pkt.haslayer(Dot11Beacon):
    radioTap = pkt.getlayer(Dot11)
    temp = radioTap.getlayer(Dot11Elt)

    if temp:
      if temp.info == xtics['essid']: # essid
        bssid = radioTap.addr2 # bssid
        channel = str(get_channel(temp.payload.payload.info)) # channel

        # detection rogue
        xtics['bssid'] = xtics['bssid'].lower()
        if (xtics['channel'] == channel) and (xtics['bssid'] == bssid):
          #print('authorized AP')
          pass
        else:
          #print('Rogue detected')
          #print(bssid + '\t' + channel)
          execution_time = time.time() - start
          #print(execution_time)
          single.insert({
            'aps': 0,
            'exec': execution_time,
            'memory': get_usage()
          })
          #get_usage()
          #print('\n')

if __name__ == '__main__':
  while True:
    start = time.time()
    sniff(iface='mon0', count=1, prn=packetHandler)