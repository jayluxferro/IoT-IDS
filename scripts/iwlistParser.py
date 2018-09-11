#!/usr/bin/python3

import subprocess
from time import sleep
import sys

wlan = "wlan0"
cells = []

def generateData():
    if len(sys.argv) == 2:
        wlan = sys.argv[1] # setting wireless scanning interface

    if subprocess.Popen("iwlist " + wlan + " scanning > iwlist", shell=True):
        return True
    else:
        return False


def checkIfCell(data):
    # receiving stripped data
    if data.split(" ")[0] == "Cell":
        return True
    else:
        return False

def getCellMac(data):
    return data.split("Address:")[1].strip()


if generateData():
    print("Please wait...")
    sleep(4)
    print("Data generated")

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

print(cells)
print("Found: " + str(len(cells)) + " APs")
