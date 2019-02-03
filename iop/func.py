#!/usr/bin/python

"""
Author: Jay Lux Ferro
Default functions
"""
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
from binascii import hexlify


def genDefaultKeys(length=1):
    random_generator = Random.new().read
    rsakey = RSA.generate(1024 * length, random_generator)
    return rsakey.exportKey('PEM'), rsakey.publickey().exportKey('PEM')


def encrypt(pubKey, data):
    try:
        pubRSAKey = RSA.importKey(pubKey)
        pubCipher = PKCS1_OAEP.new(pubRSAKey.publickey())
        return pubCipher.encrypt(data)
    except ValueError:
        return None


def decrypt(privKey, data):
    try:
        rsakey2 = RSA.importKey(privKey)
        privCipher = PKCS1_OAEP.new(rsakey2)
        return privCipher.decrypt(data)
    except ValueError:
        return None


def deviceId():
    return "302e393733393732393635353432"
