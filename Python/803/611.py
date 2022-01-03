from datetime import date

d1, m1, y1 = map(int, input().split("/"))
oy1 = date(y1, m1, d1)
oy2 = date(2022, 1, 1)

farq = oy2 - oy1

print(farq.days)

