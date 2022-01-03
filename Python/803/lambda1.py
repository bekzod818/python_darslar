# def myfunction(n):
#     return lambda x, y: n * (x + y)

# a = myfunction(5)
# print(a(2, 3))
















# ab = lambda *args: sum(args) / len(args)

# print(ab(3, 5, 4))



















lst = [1, -2, 4, 9, 0, 5, 10]

# def get_filter(a, filter=None):
#     if filter is None:
#         return a
#     res = []
#     for i in a:
#         x = filter(i)
#         res.append(x)
    
#     return res

# r = get_filter(lst, lambda x: x + 5)
# print(r)

def even(function):
    def wrapper(s):
        n = function(s)
        if n % 2 == 0:
            return "Juft"
        else:
            return "Toq"
    return wrapper




def kvsum(function):
    def wrapper(lst):
        l = function(lst)
        s = 0
        for i in l:
            s += i ** 2
        return s
    return wrapper


@even
@kvsum
def juft(lst):
    l = []
    for i in lst:
        if i % 2 == 0:
            l.append(i)
    return l


print(juft([1,2,3,4,5,6]))




lst = [4, -2, 0, 5, -9, 6, 16, -5, 11]