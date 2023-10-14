
""" 

Quadratic Residue is:
If there is a prime number 'p' and a given integer 'x', if for any number 'a' less than 'p' there exists any a^2 ≡ x mod p; x will be a 
quadratic residue of p.w

 """


def is_quadratic_residue(x, p):
    for i in range(1, p):
        if (i * i) % p == x:
            return True
    return False

def where_residue(x, p):
    quadratic_roots = []
    for i in range(1, p):
        if (i * i) % p == x:
            quadratic_roots.append(i)
    return quadratic_roots

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

p = int(input("Enter p: "))
a = int(input("Enter a: "))
is_prime_number = is_prime(p)

if is_prime_number:
    is_residue = is_quadratic_residue(a, p)

    if is_residue:
        print(f"{a} is a quadratic residue for {p}")
        quadratic_roots = where_residue(a, p)
        print("Roots are:")
        for root in quadratic_roots:
            print(root)
    else:
        print(f"{a} is not a quadratic residue for {p}")
else:
    print(f"{p} is not a prime number!")
