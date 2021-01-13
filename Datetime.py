from datetime import date, time, datetime

# Sana
yesterday = date(2021, 1, 4)
print(yesterday)

today = date.today()
print(f"Bugun {today.day}.{today.month}.{today.year}")

# Vaqt
time1 = time()
time2 = time(16, 25)
time3 = time(14, 23, 54)
print(time1, time2, time3)

# Sana va vaqt
deadline = datetime(2021, 1, 12, 23, 59, 59)
print(deadline)

# Hozirgi vaqtni chiqarish
now = datetime.now()
print(now)
print(now.date())
print(now.time())
print(f"Hozirgi vaqt {now.hour}:{now.minute}:{now.second}. Sana {now.day}.{now.month}.{now.year}")
print("-" * 35)

# Satrdan sanaga o'tkazish
deadline1 = datetime.strptime("22/05/2021 18:46", "%d/%m/%Y %H:%M")
deadline2 = datetime.strptime("13-6-2013 9/35/23", "%d-%m-%Y %H/%M/%S")
print(deadline1)
print(deadline2)
print("-" * 35)

# Sana va vaqtni formatlash
now = datetime.now()
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d-%B %A"))
print(now.strftime("%H dan %M minut o'tdi"))

