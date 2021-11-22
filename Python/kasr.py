def computeGcd(a, b):
    if b == 0:
        return a
    else:
        return computeGcd(b, a%b)

a, b = map(int, input().split())

butun = a // b

surat = a - butun * b

maxraj = b

ekub = computeGcd(surat, maxraj)
maxraj /= ekub
surat /= ekub
if a % b == 0:
    print(butun)
else:
    print(f"{butun} {int(surat)}/{int(maxraj)}")