import functools
temps = [25,39,52,68,20,89]
temp_greatest_value = functools.reduce(lambda x,y: x if(x > y ) else y,temps)
print('The greatest value in the list is '+ str(temp_greatest_value))
