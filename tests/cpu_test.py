#!/usr/bin/python

import os
import psutil

p = psutil.Process(os.getPid())
print(p.cpu_percent(interval=0))
