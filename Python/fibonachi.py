def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# n = int(input('n = '))

# if n < 0:
#     print('Bunday Fibonachi soni yo\'q')
# else:
#     for i in range(n):
#         print(fib(i))


def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = int(input(f"Talaba {ism}ning bahosini kiriting: "))
        baholar[ism] = baho
    return baholar

# n = int(input('n = '))
# l = [1, 1]

# for i in range(2, n):
#     l.append(l[i - 1] + l[i - 2])

# print(l)
pi = 3.1415