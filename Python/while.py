i = 1
label = True
while label:
    n = input('Yoshingiz nechada: ')
    # i += 1
    if n == 'exit':
        label = False
    # if i == 5:
    #     continue
    print(f"Sizning yoshingiz {n} da.")
else:
    print('Siz exit qildingiz')