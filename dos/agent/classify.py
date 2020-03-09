#!/usr/bin/python

"""
Classifier
"""
import logger as d
import pprint
import pickle
import db
import time
import numpy as np
import db
import netfilter as nf

def classify(pkt, proto, node, timeSeen, id):
    pprint.pprint(pkt)
    d.default('[-] Classifying: {}, {}, {}, {}'.format(proto, node, timeSeen, id))
    pprint.pprint(pkt)
    output = 0
    md = model()
    print(md)
    nPkts = 0
    for x in db.getCData(time.time(), proto, node):
        nPkts += 1
        output +=  -1 if md.predict(np.array([[x['cpu_percent'], x['mem_p']]]))[0] == 0 else 1

    if nPkts >= 4:
        if output == 0:
            d.success('[-] No DoS')
        else:
            d.error('[+] DoS Attack ooooo ')
            db.addDetection(node, proto, time.time() - timeSeen)
            nf.filter(pkt, proto, node, timeSeen, id)
    else:
        d.warning('[-] Can\'t decide: {} pkts'.format(nPkts))

def model():
    with open('model.pkl', 'rb') as file:
        return pickle.load(file)
