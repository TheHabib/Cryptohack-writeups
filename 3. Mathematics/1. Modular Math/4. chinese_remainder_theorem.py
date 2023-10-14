
""" 

X = ?
X = (aM1M1^-1 + aM2M2^-1 + ... + aMnMn^-1)
M = m1 * m2 * m3 * ... * mn
M1 = M/m1; M2 = M/m2; Mn = M/mn
Mn*Mn^-1 = 1 mod mn

the values of m HAS to be relatively prime


 """
 
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def modular_inverse(g, p):
    gcd, x, y = extended_gcd(g, p)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % p




def calculate_M(cm):
    cal_sum = 1
    for i in range(len(cm)):
        cal_sum *= cm[i]
    return cal_sum
        

def calculate_Mn(M, cm):
    Mn = []
    for i in range(len(cm)):
        Mn.append(int(M/cm[i]))
    return Mn



num = int(input("Enter Number of Equations: "))
ca = []
cm = []
Mn = []
Minverse = []

for i in range(num):
    ca.append(int(input(f"Enter a{i+1} : ")))
    cm.append(int(input(f"Enter m{i+1} : ")))
    
M = calculate_M(cm)

Mn = calculate_Mn(M, cm)


    
for i in range(len(Mn)):
    Minverse.append(int(modular_inverse(Mn[i], cm[i])))
    
Xcalc = []

for i in range(len(Mn)):
    Xcalc.append(int(ca[i]*Mn[i]*Minverse[i]))
    
Xsum = 0
for i in range(len(Xcalc)):
    Xsum += Xcalc[i]
    
X = Xsum % M

print(X)


""" print(f"M = {M}")

for i in range(len(Mn)):
    print(f"M{i+1} = {Mn[i]}")
    
for i in range(len(Minverse)):
    print(f"M{i+1}^-1 = {Minverse[i]}") """