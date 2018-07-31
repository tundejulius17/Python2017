num1=1
num2=3
print(str(num1) + ' ' + str(num2), end=' ')
index=2
counter=1
while index < 20:
    if index%2==0:
        num3=num1+num2
        print(str(num3), end=' ')
        num1=2*num3
    else:
        num4=(index-counter)*3
        print(str(num4), end=' ')
        num2=num4
        counter+=1
    index+=1