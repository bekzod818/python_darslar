price = 49
txt = f"The price is {price:.2f} dollars"
print(txt)
print('%.2f' % price)

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
