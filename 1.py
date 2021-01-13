def foydalanuvchi_haqida(ismi, familiya, t_yili, yoshi, t_joyi, email_manzil='', tel_nomer='' ):
    """Foydalanuvchi haqida ma'lumot saqlovchi funksiya"""
    Foydalanuvchi = {'ism':'ismi',
                    'familiya':'familiya',
                    't_yil':'t_yili',
                    'yosh':'yoshi',
                    't_joy':'t_toyi',
                    'email_manzil':'email_manzil',
                    'tel_nomer':'tel_nomer'}
    return Foydalanuvchi

talaba = foydalanuvchi_haqida('Ulugbek','Aminboyev',1999,22,'shavot')
print(talaba)
