import math

def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        (x, y) = extended_gcd(b, a % b)
        return (y, x - (a // b) * y)

def find_p_and_s(a, b):
    gcd_value = math.gcd(a, b)
    p, s = extended_gcd(a, b)
    return (p * gcd_value, s * gcd_value)

# Example usage:
a = int(input("Input a: "))
b = int(input("Input b: "))
p, s = find_p_and_s(a, b)
print(f"p = {p}, s = {s}")
