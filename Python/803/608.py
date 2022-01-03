from datetime import datetime, date

hozir = datetime.now()
yil = date(2022, 1, 1)
farq = yil - hozir.date()

print(farq.days)

