#!/usr/bin/python

import os
import psutil
import pprint


def get_usage():
    pid = os.getpid()
    py = psutil.Process(pid)
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
