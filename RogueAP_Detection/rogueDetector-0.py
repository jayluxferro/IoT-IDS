#!/usr/bin/python3

"""
    Rogue Detection Algorithm using a parser in iwlist utility application on linux
"""


import subprocess
import time
from time import sleep
import sys
import db
import math
import func 

wlan = "wlan0"
cells = []
start = time.time()
sleep_time = 0
wlan = 'wlan1'

distance = sys.argv[2]

def generateData():
    if len(sys.argv) == 2:
        global wlan
        wlan = sys.argv[1] # setting wireless scanning interface

    p = subprocess.Popen("iwlist " + wlan + " scanning > iwlist", shell=True)
    
    (output, err) = p.communicate()
    p.wait()
    if err:
        return False
    else:
        return True


def checkIfCell(data):
    # receiving stripped data
    if data.split(" ")[0] == "Cell":
        return True
    else:
        return False

def getCellMac(data):
    return data.split("Address:")[1].strip()


if generateData():
    # parsing data 
    iwlist = open('iwlist')
    data = iwlist.readlines()
    
    parserCount = 0
    cellIndex = -1
    cellBssid = None

    for x in data:
        if parserCount is 0:
            # skip first iteration
            pass
        else:
            currentData = x.strip()
            
            # check if it's the beginnning of a cell
            if checkIfCell(currentData):
                cellBssid = getCellMac(currentData)
                cells.append({ 'bssid': cellBssid })
                cellIndex += 1
            else:
                if cellBssid is not None:
                    iterData = currentData.split(":")
                    if len(iterData) == 2:
                        # formatting data
                        iData0 = iterData[0]
                        iData1 = iterData[1]

                        if iData0 == "Protocol":
                            iterData[1] = iData1.split(".11")[1]

                        if iData0 == "Frequency":
                            dat = iData1.split("GHz")
                            iterData[1] = dat[0].strip()
                            iChannel = dat[1].strip()

                            # retrieving channel parameter 
                            cData = iChannel.split(" ")
                            cells[cellIndex].update({cData[0][1:].strip().lower(): cData[1][:-1]})

                        if iData0 == "Bit Rates":
                            iterData[1] = iData1.split("Mb/s")[0].strip()


                        if iData0 == "Extra":
                            wpaData = iData1.split("=")
                            if len(wpaData) == 2:
                                iterData[0] = wpaData[0].strip().lower()
                                iterData[1] = wpaData[1]

                            if wpaData[0] == "":
                                continue



                        cells[cellIndex].update({"_".join(iterData[0].strip().split(" ")).lower().replace("_(1)", ""): iterData[1].strip()})
                    elif len(iterData) == 1:
                        # quality and signal level
                        qsData = iterData[0].split("  ")
                        if len(qsData) == 2:
                            quality = qsData[0].split("=")
                            level = qsData[1].split("=")
                            cells[cellIndex].update({"_".join(quality[0].split(" ")).lower(): quality[1].split("/")[0].strip(), "_".join(level[0].split(" ")).lower(): level[1].split("dBm")[0].strip()})

                        
                    

        parserCount += 1

# init
device = db.get_ap()
xtics = {
	'id': device[0],
	'group_cipher': str(device[1]),
	'protocol': str(device[2]),
	'bssid': str(device[3]),
	'quality': str(device[4]),
	'encryption_key': str(device[5]),
	'pairwise_ciphers': str(device[6]),
	'frequency': str(device[7]),
	'rsn_ie': str(device[8]),
	'essid': str(device[9]),
	'bit_rates': str(device[10]),
	'fm': str(device[11]),
	'signal_level': str(device[12]),
	'ie': str(device[13]),
	'authentication_suites': str(device[14]),
	'channel': str(device[15]),
	'mode': str(device[16]),
	'entropy': device[17]
}
entropy = xtics['entropy']

"""
	0 : id
	1 : group_cipher
	2 : protocol
	3 : bssid
	4 : quality
	5 : encryption_key
	6 : pairwise_cipher
	7 : frequency
	8 : rsn_ie
	9 : essid
	10: bit_rates
	11: fm
	12: signal_level
	13: ie
	14: authentication_suites
	15: channel
	16: mode
	17: entropy
"""

aps = len(cells)
ap = [xtics]
for ap_info in ap:
    # searching through scanned data
    for data in cells:
        if(data['essid'].strip('\"') == ap_info['essid']):
            entropy = (-(1.0/14) * math.log(1.0/14, 2)) # for essid
            """
            /**
            * @param
            * group_cipher, protocol, bssid, encryption_key, pairwise_ciphers, frequency, rsn_ie, essid, bit_rates, fm, ie, authentication_suties, channel, mode 
            */
            """
            if ap_info['group_cipher'] == data['group_cipher']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['protocol'] == data['protocol']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['bssid'] == data['bssid']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['encryption_key'] == data['encryption_key']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['pairwise_ciphers'] == data['pairwise_ciphers']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['frequency'] == data['frequency']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['rsn_ie'] == data['rsn_ie']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['bit_rates'] == data['bit_rates']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['fm'] == data['fm']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['authentication_suites'] == data['authentication_suites']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['channel'] == data['channel']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if ap_info['mode'] == data['mode']:
                entropy += (-(1.0/14) * math.log(1.0/14, 2))

            if entropy != ap_info['entropy']:
                execution_time = time.time() - start
                db.log(aps, execution_time, func.get_usage(), entropy, 0, distance)
