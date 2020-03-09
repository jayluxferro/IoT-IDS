from fastecdsa import keys, curve, ecdsa

#generating the private key over secp224k1 curve
private_key = keys.gen_private_key(curve=curve.secp224k1)

#get the public key from the corresponding private key
public_key = keys.get_public_key(private_key, curve=curve.secp224k1)

msg = "Sign this message with secp224k1"


r, s = ecdsa.sign(msg, private_key, curve.secp224k1)

print(r)
print(s)

print(ecdsa.verify((r, s), msg, public_key, curve.secp224k1))