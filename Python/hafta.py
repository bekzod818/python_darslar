def hafta(kun):
    s = ''
    if kun % 7 == 0:
        s = 'Yakshanba'
    elif kun % 7 == 1:
        s = 'Dushanba'
    elif kun % 7 == 2:
        s = 'Seshanba'
    elif kun % 7 == 3:
        s = 'Chorshanba'
    elif kun % 7 == 4:
        s = 'Payshanba'
    elif kun % 7 == 5:
        s = 'Juma'
    else:
        s = 'Shanba'
    return s

print(hafta(15))