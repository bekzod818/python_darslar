from datetime import date, time, datetime

# today = date.today()
# yesterday = date(2021, 10, 30)

# print(f"Bugun: {today}")
# print(f"Ertaga: {yesterday}")

# print(today.year, today.month, today.day)

# time1 = time(15, 17, 15)
# print(time1)

now = datetime.now()
print(now.strftime("%d-%B %A"))
print(now.strftime("%c"))

print(now.strftime("%H dan %M minut o'tdi."))
# print(now.date())
# print(now.time())

# print(now.month, now.year)
# print(now.hour, now.minute, now.second)

# deadline = datetime.strptime("31 December 2021 23:59", "%d %B %Y %H:%M")
# print(deadline)

