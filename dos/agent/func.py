#!/usr/bin/python
"""
Functions
"""
import subprocess
import db
import psutil

def inSubnet(ip):
    subnet = db.getSubnet()['ip'].encode('utf-8')
    # classful
    subnet = subnet.split('/')
    c = subnet[-1]
    r = int(int(c)/8)
    ip = ip.split('.')
    subnet = subnet[0].split('.')
    if subnet[:r] == ip[:r]:
        return True
    return False

def setSubnet(iface):
    sw = subprocess.check_output(['ip','addr','show',iface], shell=False)
    gw = sw.splitlines()[2].split(' ')[5]
    mac = sw.splitlines()[1].split(' ')[5]
    db.setSubnet(gw, mac)   

def tau():
    return 0.6

# OS Kernel Info
def cpu_percent():
    return psutil.cpu_percent() # default value is already a percentage

def cpu_count():
    return psutil.cpu_count() # number of logical CPUs

def cpu_freq():
    cpuData = psutil.cpu_freq()
    return (cpuData.current, cpuData.min, cpuData.max) # current, min, max

def cpu_stats():
    data = psutil.cpu_stats()
    return (data.ctx_switches, data.interrupts, data.soft_interrupts, data.syscalls) # ctx_switches, interrupts, soft_interrupts, syscalls

def mtu(iface='eth0'):
    return psutil.net_if_stats()[iface].mtu # in bytes

def battery():
    return psutil.sensors_battery().percent  # in percentage

def fan():
    speed = []
    data = psutil.sensors_fans()
    for x in data:
       speed.append(data[x][0].current)

    if len(speed) > 0:
        return np.average(speed)
    else:
        return 0 # rounds per minutes


def temperature():
    data = psutil.sensors_temperatures()['coretemp'][0]
    return (data.current, data.high, data.critical)

def swap_memory():
    data = psutil.swap_memory()
    return (data.total, data.used, data.free, data.percent) # in bytes; total, used, free, percent)

def memory():
    data = psutil.virtual_memory()
    return (data.total, data.available, data.percent, data.used, data.free); # in bytes; (total, available, percent, used, free)

