import numpy as np

key_value = input("Kalit matnini kiriting: key = ")

key_hex = []

for i in key_value:
    index = ord(i)
    key_hex.append(hex(index))
#print(key_hex)
hexdecimal = []
for item in key_hex:
    index2 = item[2:]
    hexdecimal.append(index2)

print(hexdecimal)

res = []
for i in range(4):
    new = []
    for j in range(i, 16, 4):
        new.append(hexdecimal[j])
    res.append(new)
    
arr = np.array(res)
print(arr)
