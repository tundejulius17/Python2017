# Here we ask the name of a file
filename = input('Enter file name: ')

try:

    infile = open(filename, 'r')

    list = infile.readlines()

    print('number of products:')

    numberOfProduct = len(list)

    print(numberOfProduct)

    sum = 0

    print('The total of each product:')

    for i in range(len(list)):
        attValuesList = list[i].split(';')
        totalValue = eval(attValuesList[1]) * eval(attValuesList[2])
        print(totalValue)
        sum += totalValue

    print('The sum of all products:')
    print(sum)




except  IOError:
    print('IOError: ' + 'File not found')

except TypeError:
    print('Cannot sum text with number! ')

else:
    print('The program was executed successfully')
