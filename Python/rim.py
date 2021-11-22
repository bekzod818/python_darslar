def rimraqam(n):
    res = ""
    if n >= 1000:
        butun = n // 1000
        res += butun * "M"
        n %= 1000

    if n >= 900 and n < 1000:
        res += "CM"
        n %= 900

    if n >= 500:
        butun = n // 500
        res += butun * "D"
        n %= 500

    if n >= 400 and n < 500:
        res += "CD"
        n %= 400

    if n >= 100:
        butun = n // 100
        res += butun * "C"
        n %= 100

    if n >= 90 and n < 100:
        res += "XC"
        n %= 90

    if n >= 50:
        butun = n // 50
        res += butun * "L"
        n %= 50

    if n >= 40 and n < 50:
        res += "XL"
        n %= 40

    if n >= 10:
        butun = n // 10
        res += butun * "X"
        n %= 10

    if n == 9:
        res += "IX"
        n = 0

    if n >= 5:
        butun = n // 5
        res += butun * "V"
        n %= 5

    if n == 4:
        res += "IV"
        n = 0

    if n >= 1:
        butun = n
        res += butun * "I"
    
    return res

n = int(input())
print(rimraqam(n))
