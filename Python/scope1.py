x = 300

def myfunc():
    global x
    x = 50
    print(x + 600)

myfunc()

print(x)








# def myfunc():
#     x = 300
#     def myinnerfunc():
#         return x
#     return myinnerfunc()

# print(myfunc())