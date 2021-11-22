def kvkub(n):
    kv = n ** 2
    kub = n ** 3
    return f"Kvadrati: {kv}\nKubi: {kub}"

a = int(input('Son kiriting:'))

print(kvkub(a))