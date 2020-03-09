#!/usr/bin/python

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random

message = "Testing"
random_generator = Random.new().read
rsakey = RSA.generate(1024, random_generator)
pubCipher = PKCS1_OAEP.new(rsakey.publickey())
privCipher = PKCS1_OAEP.new(rsakey)

pubKey = rsakey.publickey().exportKey('PEM')
privKey = rsakey.exportKey('PEM')
print(privKey)



rsakey2 = RSA.importKey(privKey)
pubCipher2 = PKCS1_OAEP.new(rsakey2.publickey())
privCipher2 = PKCS1_OAEP.new(rsakey2)


pubRSAKey = RSA.importKey(pubKey)
pubCipher = PKCS1_OAEP.new(pubRSAKey.publickey())


ciphertext = pubCipher.encrypt(message)
#print("Encrypted Message: " + ciphertext)
print(len(ciphertext))

print("Decrypted Message: " + privCipher.decrypt(ciphertext))
print("Decrypted Message: " + privCipher2.decrypt(ciphertext))