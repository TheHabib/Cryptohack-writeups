from pwn import xor
x1 = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
#flag = "cryptO{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}"
#key = "myXORKeymyXORkeymyXORkeymyXORkeymyXORkeymy"
x1_conv = bytes.fromhex(x1)

x2 = b"crypto{"
x3 = xor(x1_conv, x2)

x4 = xor(x1_conv, x3)
print(x4)
x5 = xor(x1_conv, x4)
print(x5)
x5 = xor(x1_conv, b'myXORkey')
print(f"X5 is: {x5}")