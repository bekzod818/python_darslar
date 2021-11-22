w, d = map(float, input().split())

if w > d:
    print('>')
elif w < d:
    print('<')
else:
    print('=')