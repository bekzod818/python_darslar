def factorial(n):
    """n! ni hisoblash funksiyasi"""
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p


print(factorial(6))



"""
n! = 1 * 2 * 3 ... * n

n! = (n-1)! * n
5! = 1 * 2 * 3 * 4 * 5
4! = 1 * 2 * 3 * 4


5! = 4! * 5
"""

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(3))


"""
f0 = 0
f1 = 1
f2 = 1 = f0 + f1
f3 = 2 = f1 + f2
f4 = 3 = f2 + f3
f5 = 5 = f3 + f4
f6 = 8 = f5 + f4
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(20))








# def f(n):
#     """Bu funksiya n dan 1 gacha sonlarni chiqaradi"""
#     if n == 0:
#         return
#     else:
#         print(n)
#         f(n - 1)

# f(4)