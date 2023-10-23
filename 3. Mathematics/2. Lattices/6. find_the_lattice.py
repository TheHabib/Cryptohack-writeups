""" 
In this cryptography, we are given a two-dimensional vector in a lattice, (q, h)

The lattice is defined by the basis vectors (1, h) and (0, q).

First we gotta use gaussian lattice reduction for 2d vectors and find 

The shortest vector in this lattice is likely to be the secret key. In order to decrypt the flag, we need to find the shortest vector in the lattice.

Use gaussian lattice reduction to find the shortest vector. You will get a vector (f, g) which are the private key.

So, you will have public keypair (q, h) and private keypair (f, g) and encrypted message (e).

Then just run the decrypt function from the given python source code and you will get your flag.

 """
 
 

"""  
 
Given source program is:
    
from Crypto.Util.number import getPrime, inverse, bytes_to_long
import random
import math

FLAG = b'crypto{?????????????????????}'

def gen_key():
    q = getPrime(512)
    upper_bound = int(math.sqrt(q // 2))
    lower_bound = int(math.sqrt(q // 4))
    f = random.radint(2, upper_bound)
    
    while True:
        g = random.radint(lower_bound, upper_bound)
        if math.gcd(f, g) == 1:
            break
        
    h = (inverse(f, q)*g) % q
    return (q, h), (f, g)

def encrypt(q, h, m):
    assert m < int(math.sqrt(q // 2))
    r = random.randint(2, int(math.sqrt(q // 2)))
    e = (r*h + m) % q
    return e

def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m

public, private = gen_key()
q, h = public
f, g = private

m = bytes_to_long(FLAG)
e = encrypt(q, h, m)

print(f'Public key: {(q,h)}')
print(f'Encrypted Flag: {e}')


 """      
        
""" 
    
Public Key = (7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257, 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800)
Encrypted Flag = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

 """



def long_to_bytes(long_digit):
    byte_length = (long_digit.bit_length() + 7) // 8
    return long_digit.to_bytes(byte_length, byteorder='big')


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
    
def modinv(a, m):
    g, x, y = egcd(a, m)
    
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % m
    
def find_m(a, f, g):
    return (a * modinv(f, g)) % g


def mag_sqr(A):
    xxyz = pow(A[0], 2) + pow(A[1], 2)
    return pow(xxyz, 0.5)

def dot_prod(A1, A2):
    return ((A1[0] * A2[0]) + (A1[1] * A2[1]))

def gaussian_lattice_reduction(V1, V2):
    while True:
        if (mag_sqr(V2) < mag_sqr(V1)):
            V1, V2 = V2, V1 #swaps
            
        m = int((dot_prod(V1, V2) / dot_prod(V1, V1)))
        
        if (m == 0):
            return V1, V2
        
        #V2 = V2 - m * V1
        V3 = []
        for i in range(len(V1)):
            V3.append(V1[i]*m)
            
        for i in range(len(V2)):
            V2[i] = V2[i] - V3[i]
            
def decrypt(q, f, g, e):
    a = (f*e) % q
    m = find_m(a, f, g)
    return m

q = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257

h = 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800

e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

vector_1 = [1, h]
vector_2 = [0, q]

reduced_vector1, reduced_vector2 = gaussian_lattice_reduction(vector_1, vector_2)

if(mag_sqr(reduced_vector1) > mag_sqr(reduced_vector2)):
    reduced_vector = reduced_vector2
    
else:
    reduced_vector = reduced_vector1
    
f = reduced_vector[0]
g = reduced_vector[1]

#Use q, f, g, e in decrypt function to get flag

print(f)
print(g)

print(decrypt(q,f,g,e))
print(long_to_bytes(decrypt(q,f,g,e)))