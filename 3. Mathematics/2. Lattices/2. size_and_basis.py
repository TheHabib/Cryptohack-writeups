v = [4, 6, 2, 5]

size = 0

for i in range(len(v)):
    size += pow(v[i], 2)

size = int(pow(size, 0.5))

print(size)