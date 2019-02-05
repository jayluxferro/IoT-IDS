#!/usr/bin/python
"""
Author: Jay Lux Ferro
Description: Logging
Date: 29th Dec 2018
"""

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def header(text):
    print(HEADER + text + ENDC)


def default(text):
    print(OKBLUE + text + ENDC)


def success(text):
    print(OKGREEN + text + ENDC)


def warning(text):
    print(WARNING + text + ENDC)


def error(text):
    print(FAIL + text + ENDC)


def bold(text):
    print(BOLD + text + ENDC)


def underline(text):
    print(UNDERLINE + text + ENDC)
