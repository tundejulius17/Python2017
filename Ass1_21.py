x = 0
y = 1

print(str(y), end=' ')

z = x+y

start = 1
stop = 10

for num in range(start, stop):
    #if num < stop:
        print(str(z), end=' ')
        x=y
        y=z
        z=x+y




