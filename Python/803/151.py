from datetime import datetime

hozir = datetime.now()

kun = datetime(1,1,1)

farq = hozir - kun
d = farq.days
s = farq.seconds

print(d * 24 * 60 * 60 + s)