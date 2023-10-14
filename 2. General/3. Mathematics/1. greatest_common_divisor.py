def gcd_calc(big, small):
    temp = big % small
    if temp == 0:
        return small
    else:
        return gcd_calc(small, temp)

print("Input two digits: ")
x1 = int(input())  # Convert user input to integer
x2 = int(input())

if x1 < x2:
    big = x2
    small = x1

else:
    big = x1
    small = x2


gcd = gcd_calc(big, small)
print(gcd)