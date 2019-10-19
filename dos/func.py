#!/usr/bin/python
"""
Functions
"""
import subprocess
import logger as log
import db
import psutil
import numpy as np

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


def getInterPacketArrival(info):
    res = []
    counter = 0
    holder = 0
    for x in info:

        if counter % 2 == 0:
            # the first number
            holder = x
        else:
            res.append(abs(x - holder))
        counter = counter + 1

    return res

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



def getAdditionalParams():
    data = []
    # freq_c, freq_min, freq_max, cpu_percent, ctx_switches, interrupts, soft_interrupts, syscalls, mtu, battery, fan, temp_c, temp_h, temp_crit, swap_t, swap_u, swap_f, swap_p, mem_t, mem_a, mem_p, mem_u, mem_f
    # 23 params
    for _ in cpu_freq(): data.append(_)
    data.append(cpu_percent())
    
    for _ in cpu_stats(): data.append(_)
    data.append(mtu())
    data.append(battery())
    data.append(fan())

    for _ in temperature(): data.append(_)
    for _ in swap_memory(): data.append(_)
    for _ in memory(): data.append(_)

    return tuple(data)

def trimOutliers(data, iterations):
    for _ in range(iterations):
        data.remove(np.max(data))

    return data
