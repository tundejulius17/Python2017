start = 1
stop = 249

sum = 0

for number in range(start, stop):
    if number % 2 != 0:
        sum += number

    print(str(number) + ' ', end='')

print()
print("Sum of all odd numbers in the interval [1, 249]: " + str(sum))
