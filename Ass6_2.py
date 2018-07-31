import re

text = "name=Milk;amount=200;unit_price=0.9\nname=Bread;amount=134;" \
       "unit_price=3.48\nname=Butter;amount=58;unit_price=1.65\nname=Cheese;" \
       "amount=260;unit_price=4.35"

products = re.split("\n", text)
#print(products)
sum = 0
for i in products:
    product = re.split(";",i)
    print(product)
    amount = product[1].split('=')[1]
    unit_price = product[2].split('=')[1]
    sum += eval(amount) * eval(unit_price)

print("Total sum of all products: " + str(sum))