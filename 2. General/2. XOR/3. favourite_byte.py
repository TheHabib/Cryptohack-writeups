from pwn import *
x1 = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
x1_x = bytes.fromhex(x1)
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

""" for i in range(len(alph)):
    temp = alph[i]
    z = xor(x1_x, temp)
    print(z) """

for i in range(99):
    print(i)
    z = xor(x1_x, i)
    print(z)