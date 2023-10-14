#This code decodes SSH / RSA public key

from Crypto.PublicKey import RSA
with open("bruce_rsa.pub", 'r') as file:
    data = file.read()
key = RSA.import_key(data)
print(key.n)

"""
Why n? Because public keypair of rsa is {n, e}. 
The question asked for the modulus n as a decimal integer from Bruce's SSH public key.
So, got n.
"""