'''
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ['watarmelon']
thislist.insert(2, 'orange')
thislist.append('cherry')
tropical = ['mango', 'pineapple', 'papaya'] # thistuple = ('mango', 'pineapple', 'papaya')
thislist.extend(tropical)
#print(thislist)
thislist.remove('mango')
thislist.pop(2)
del thislist[0]
#print(thislist)
#[print(x) for x in thislist]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if 'n' in x]
newlist_1 = [x.upper() for x in fruits if x == 'apple']
newlist_2 = [x for x in range(1, 11) if x < 5]
newlist_3 = ['hello' for x in fruits]
newlist_4 = [x if x != 'banana' else 'orange' for x in fruits]
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)
# print(newlist)
# print(newlist_1)
# print(newlist_2)
# print(newlist_3)
# print(newlist_4)
def myfunc(n):
    return abs(n - 50)
numbers = [100, 50, 65, 82, 23]
numbers.sort(key=myfunc)
print(numbers)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
thislist.reverse()
#print(thislist)

# copy list
#mylist = thislist.copy()
#mylist = list(thislist)
mylist = thislist[:]
print(mylist) 

#join list
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)
# for x in list2:
#     list1.append(x)
# print(list1)
list1.extend(list2)
print(list1)

#Misol
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = []
odd = listOne[1::2]
even = listTwo[0::2]
print(f'Royhatda juft orinda turgan elementlar: {odd}')
print(f"Royhatda toq orinda turgan elementlar: {even}")
listThree.extend(odd)
listThree.extend(even)
print(listThree)

# Listga element kiritish
n = int(input())
lst = list(int(item) for item in input().split())[:n]
print(max(lst))
print(list(range(1,50,4)))
print("""Bekzod
Raximov""")
'''
x, y = input().split()
x = int(x)
y = int(y)
z = x / y + x ** y - x // y
print("%.2f" % z)

