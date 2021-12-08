# num = [23, 24, "hello", 54, 34]
# cnt = 0
# for i in num:
#     # print(i, end=" ")
#     cnt += 1
# # print(cnt)

# x = [2,3,4,5,6]


# num = ["Hello", 24, 45, "", 54]
# # a = input("So'z kiriting: ")
# num.remove("")
# # num.insert(-1, a)
# # print(num)




# # l = [10, 5, 7, 9, 23, 15]
# # l.sort()
# # for i in l:
# #     if i % 5 == 0:
# #         print(i, end=" ")




# num = [2, 8, 2, 4, 7, 3]

# num.sort(reverse=True)

# print(num[0])


# s = 0

# for i in num:
#     s += i
# print(s)


# num = [2, 3, 4, 5, 2, 6, 3, 2]

# num = set(num)
# num = list(num)
# print(num)

# import random

# print(random.choice(num))



num = [2, 23, 24, 51, 46, 67]

juft = [i for i in num if i % 2 == 0]
toq = [i for i in num if i % 2]

# for i in num:
#     if i % 2 == 0:
#         juft.append(i)
#     else:
#         toq.append(i)

# print("Juft", juft, end=" ")
# print("Toq", toq)


# n = int(input("Nechta element kiritmoqchisiz: "))

# l = []
# i = 1

# while i <= n:
#     item = input(f"{i} - mahsulotni kiriting: ")
#     l.append(item)
#     i += 1

# for i in range(1, n + 1):
#     item = input(f"{i} - mahsulotni kiriting: ")
#     l.append(item)

# print(l)



num = [2,3,4,3,2,6,5,3,2]
yakka = []

for i in range(len(num)):
    if num[i] not in yakka:
        yakka.append(num[i])
    else:
        pass

print(yakka)



