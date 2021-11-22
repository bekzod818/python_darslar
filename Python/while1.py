from datetime import datetime

now = datetime.now()

while True:
    msg = input("Nechanchi yil tug'ilgansiz (to'xtatish uchun - exit): ")
    if msg == "exit":
        break
    else:
        yosh = now.year - int(msg)
        print(f"Sizning yoshingiz {yosh}da.")