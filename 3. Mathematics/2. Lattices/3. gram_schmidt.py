
""" 

Sage has in built function for gram-schmidt:
    
sage: v0 = vector([4,1,3,-1])
sage: v1 = vector([2,1,-3,4])
sage: v2 = vector([1,0,-2,7])
sage: v3 = vector([6,2,9,-5])
sage: M = Matrix([v0,v1,v2,v3])
sage: M.gram_schmidt()

 """



import numpy as np

# Define the input vectors
v = [
    np.array([4, 1, 3, -1]),
    np.array([2, 1, -3, 4]),
    np.array([1, 0, -2, 7]),
    np.array([6, 2, 9, -5])
]

# Initialize the list of orthogonalized vectors with the first vector
u = [v[0]]

# Loop through the remaining vectors
for vi in v[1:]:
    mi = []  # List to store μij values
    for uj in u:
        #print(f"uj = {uj}")
        dot_product = np.dot(vi, uj)
        #print(f"dot product of {uj} and {vi} is {dot_product}")
        norm_squared = np.dot(uj, uj)
        #print(f"morm squared of {dot_product} is {norm_squared}")
        mi.append(dot_product / norm_squared)
    
    # Calculate the next orthogonalized vector vi
    ui = vi - sum([mij * uj for mij, uj in zip(mi, u)])
    
    # Append the orthogonalized vector to the list
    u.append(ui)

# Print the value of the second component of the fourth orthogonalized vector
result = round(u[3][1], 5)
print(result)
