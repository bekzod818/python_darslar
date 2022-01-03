def kubsum(func):
    def wrapper(p):
        s = 0
        lst = func(p)
        for i in lst:
            s += i ** 3
        return s
    return wrapper


def text(function):
    def add(p):
        s = ""
        lst = function(p)
        for i in lst:
            s += i
            s += " "
        return s
    return add


@kubsum
def get_int(lst):
    p = []
    for i in lst:
        if isinstance(i, int):
            p.append(i)
    return p

@text
def get_str(lst):
    p = []
    for i in lst:
        if isinstance(i, str):
            p.append(i)
    return p

# lst =["Salom", 5, 3.7, 1+2j, "Python", 4, 1e-2, "Django", -3]

# print(get_int(lst))
# print(get_str(lst))