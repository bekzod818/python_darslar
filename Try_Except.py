"""
try:
    a = int(input("a = "))
    b = int(input("b = "))
    if b == 0:
        raise Exception("Nolga bo'lish yuzaga keldi.")
    print("c = a / b = " + str(a / b))
except ValueError:
    print("Son kiritmadingiz!")
# except ZeroDivisionError:
#     print("Sonni nolga bo'lib bo'lmaydi.")
except Exception as e:
    print("Xatolik: ", e)
else:
    print("Dasturda xatolik yo'q.")
finally:
    print("Dastur tugadi.")
"""

try:
    f = open("example.txt", 'a')
    f.write("Lorem Ipsum Doler amet.")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

 






