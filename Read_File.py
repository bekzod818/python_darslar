# Faylni o'qish
"""
file = open('example.txt', 'r')
print(file.read())  # faylni to'liq o'qiydi
print(file.read(15))  # fayl boshidan 15 ta belgi o'qiydi
print(file.readline())  # faylni bitta qatorini o'qiydi
for line in file:
    print(line)

# Faylga matn qo'shish

file = open('example.txt', 'a')
file.write('Now the file has more content!')
file.close()

file = open('example.txt', 'r')
print(file.read())


# Faylga yozish
file = open('example.txt', 'w')
file.write('Woops! I have deleted the content!')
file.close()

file = open('example.txt', 'r')
print(file.read())


# Fayl yaratish
file = open('myfile.txt', 'x')
file = open('myfile.txt', 'w')
file = open('myfile.txt', 'a')
"""

# Faylni o'chirish
# import os
# os.remove('myfile.txt')
# import os
# if os.path.exists('myfile.txt'):
#     os.remove('myfile.txt')
# else:
#     print("Bunday fayl yo'q")


