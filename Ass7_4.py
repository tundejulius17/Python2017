
temps=[25,39,52,68,20,89]
# using the lambda expression
y_new_value1 = list(map(lambda x: 0 if x < 50 else x, temps))
print(y_new_value1)
y_new_value2 = list(map(lambda x: 2 if 50<x<=75 else x, temps))
print(y_new_value2)
y_new_value3 = list(map(lambda x: 3 if x>75 else x, temps ))
print(y_new_value3)
