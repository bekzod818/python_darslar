# Lokal o'zgaruvchi
def funksiya():
    x = 777  # lokal o'zgaruvchi faqat funksiya ichida ishlaydi

    # Ichki funksiya
    def ichki_funksiya():
        print(x)
    ichki_funksiya()

funksiya()

# Global o'zgaruvchi
x = 523

def funk():
    global x
    x = 207
    print(x)

funk()
print(x)

# Modul
import platform
x = platform.system()
print(x)
print(dir(platform))
print(platform.uname())
