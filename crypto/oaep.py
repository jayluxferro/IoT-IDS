#!/usr/bin/python

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random

message = "Testing"
random_generator = Random.new().read
rsakey = RSA.generate(1024, random_generator)
pubCipher = PKCS1_OAEP.new(rsakey.publickey())
privCipher = PKCS1_OAEP.new(rsakey)

print(rsakey.publickey().exportKey('PEM'))
print(rsakey.exportKey('PEM'))

ciphertext = pubCipher.encrypt(message)
print("Encrypted Message: " + ciphertext)

print("Decrypted Message: " + privCipher.decrypt(ciphertext))
