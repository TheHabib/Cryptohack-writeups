x1 = "label"
x2 = 13
#x1 = label
list_ = []
word_ = []
for i in range(len(x1)):
    p = x1[i]
    y = ord(p) ^ x2
    list_.append(y)

for i in range(len(list_)):
    word_.append(chr(list_[i]))

print(word_)