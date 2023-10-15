u = [7,7,2]
v = [2,6,3]
w = [1,0,0]

for i in range(3):
    v[i] = 2 * v[i]
    
for i in range(3):
    v[i] = v[i] - w[i]
    
for i in range(3):
    v[i] = 3 * v[i]
    
       
for i in range(3):
    u[i] = 2 * u[i]
    
sum = 0

""" 
if a vector is axi + byj + czk
and another vector is dxi + eyj + fzk

Then dot multiplication of the two 3d vectors are:
    (ax * dx) + (by * ey) + (cz + fz)

 """

for i in range(3):
    v[i] = v[i] * u[i]
    sum += v[i]
    
print(sum)