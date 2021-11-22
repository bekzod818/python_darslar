import re


# andoza = '^998[012345789][012345789][0-9]{7}$'
andoza = "^[a-z0-9_-]{5,15}$"

while True:
    sana = input("Username kiriting: ")
    result = re.match(andoza, sana)

    if result:
        print("Username to'g'ri kiritldi")
        break
    else:
        print("Yana bir bor urinib ko'ring")	
