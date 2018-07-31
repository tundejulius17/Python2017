import math

def math_sum(value_list):

    y = 0

    for i in range(len(value_list)):
        y += math.pow(math.sin(value_list[i]), 2) - math.log(value_list[i], 3) \
           + 1/math.pow(value_list[i], 5)

    return y

value_list = [90,6,8.9]
y=math_sum(value_list)

print("The result of the calculation is: ")
print('{:.2f}'.format(y))