#!/usr/bin/python
"""
Generate data file for model classification
"""

import db

handler = open('data.csv', 'w')
data = ""
# write headers
data += "cpu,memory,malicious\n"

# getting normal cpu profile
for d in db.getTable("cpu"):
    #print(d['cpu_percent'], d['mem_p'])
    data += "{},{},0\n".format(d['cpu_percent'], d['mem_p'])


# tcp
for d in db.getTable("tcp"):
    #print(d['cpu_percent'], d['mem_p'])
    data += "{},{},1\n".format(d['cpu_percent'], d['mem_p'])

# udp
for d in db.getTable("udp"):
    #print(d['cpu_percent'], d['mem_p'])
    data += "{},{},1\n".format(d['cpu_percent'], d['mem_p'])


# icmp
for d in db.getTable("icmp"):
    #print(d['cpu_percent'], d['mem_p'])
    data += "{},{},1\n".format(d['cpu_percent'], d['mem_p'])

handler.write(data)
handler.close()
