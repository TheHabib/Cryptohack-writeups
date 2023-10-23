#for 2d vectors

def mag_sqr(A):
    xxyz = pow(A[0], 2) + pow(A[1], 2)
    return pow(xxyz, 0.5)

def dot_prod(A1, A2):
    return ((A1[0] * A2[0]) + (A1[1] * A2[1]))

def gaussian_lattice_reduction(V1, V2):
    while True:
        if (mag_sqr(V2) < mag_sqr(V1)):
            V1, V2 = V2, V1 #swaps
            print(f"V1 after swap = {V1}")
            print(f"V2 after swap = {V2}")
        
        else:
            print(f"No Swap\nV1 = {V1}\nV2 = {V2}")
            
        m = int((dot_prod(V1, V2) / dot_prod(V1, V1)))
        print(f"m = {m}")
        
        if(m == 0):
            return V1, V2
        
        V3 = []
        for i in range(len(V1)):
            V3.append(V1[i]*m)
            
        for i in range(len(V2)):
            V2[i] = V2[i] - V3[i]
            
            
V1 = [846835985, 9834798552]
V2 = [87502093, 123094980]

Result_1, Result_2 = gaussian_lattice_reduction(V1, V2)

print(f"Result_1 = {Result_1}")
print(f"Result_2 = {Result_2}")

print(dot_prod(Result_1, Result_2))