
""" 
Volume of a lattice is the modulus of the determinent of matrix created by the vectors
 """


a = [6, 2, -3]
b = [5, 1, 4]
c = [2, 7, 1]

sum = (a[0] * ((b[1]*c[2]) - (b[2]*c[1]))) - (a[1] * ((b[0] * c[2]) - (b[2] * c[0]))) + (a[2] * ((b[0] * c[1]) - (b[1] * c[0])))

if(sum < 0):
    sum = sum * (-1)
    
print(sum)