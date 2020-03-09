#!/usr/bin/python

import db
import logger
from numpy import average as avg

if __name__ == "__main__":

    icmp_time = []
    udp_time = []
    tcp_time = []

    prev = 0
    for icmp in db.getP("icmp"):
        current = float(icmp['time'])
        if prev != 0:
            icmp_time.append(current - prev)
        prev = current

    logger.success("ICMP timing window: {0}".format(str(avg(icmp_time))))
    db.updatePInterval("icmp", avg(icmp_time))
    print("\n")

    prev = 0
    for udp in db.getP("udp"):
        current = float(udp['time'])
        if prev != 0:
            udp_time.append(current - prev)
        prev = current
    logger.warning("UDP timing window: {0}".format(str(avg(udp_time))))
    db.updatePInterval("udp", avg(udp_time))
    print("\n")


    prev = 0
    for tcp in db.getP("tcp"):
        current = float(tcp['time'])
        if prev != 0:
            tcp_time.append(current - prev)
        prev = current

    logger.default("TCP timing window: {0}".format(str(avg(tcp_time))))
    db.updatePInterval("tcp", avg(tcp_time))
    print("\n")
