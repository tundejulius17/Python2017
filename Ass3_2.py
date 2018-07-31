text = "name=Milk;amount=200;unit_price=0.9\n" \
       "name=Bread;amount=134;unit_price=3.48\n" \
       "name=Butter;amount=58;unit_price=1.65\n" \
       "name=Cheese;amount=260;unit_price=4.35"

products=text.split("\n")
price_sum = 0

for p in products:
    print(p)
    product_info = p.split(";")
    amount_str = product_info[1].split("=")[1]
    price_str = product_info[2].split("=")[1]
    price_sum+=eval(amount_str)*eval(price_str)


print("The total price of all products is: ")
print(str(price_sum))

