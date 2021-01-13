a = 'Hello'
a = 15
print(bool(a))
# False 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool({})
bool([])
class my_class():
    def __len__(self):
        return 0
myobj = my_class()
print(bool(myobj))

def my_func():
    return True
if my_func:
    print("YES")
else:
    print("NO")