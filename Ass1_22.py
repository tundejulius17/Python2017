a=0
b=0
c=1
print (str(c), end = ' ')
start = 1
end = 10
d=a + b + c

for x in range(start, end ):
    print(d , end =' ')
    a = b
    b = c
    c = d
    d = a + b + c