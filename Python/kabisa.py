# Bu misol kabisa yilini aniqlaydi
yil = int(input("Yilni kiriting: "))
"""
if yil % 4 != 0:
	print("Oddiy")
elif yil % 100 == 0:
	if yil % 400 == 0:
		print("Kabisa")
	else:
		print("Oddiy")
else:
	print("Kabisa")

"""
if yil % 4 != 0 or (yil % 100 == 0 and yil % 400 != 0):
	print("Oddiy")

else:
	print("Kabisa")