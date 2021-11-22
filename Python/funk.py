# print

def salom(ism, familiya):
    """Bu funksiya salom beradi"""
    print(f"{ism.title()} {familiya.title()} assalomu aleykum.")

salom('Bekzod', 'Raximov')

# return

def salom(ism, familiya):
    """Bu funksiya salom deb qaytaradi"""
    return f'{ism.title()} {familiya.title()} assalomu aleykum.'

print(salom('Bekzod', 'Raximov'))