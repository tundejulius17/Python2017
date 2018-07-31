import re
def fileLength(filename):
    'returns the number of characters in file filename'
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    return 'The number of characters in ' + filename + ' is ' + str( len(content))
    # Here we define a function for reading the file
def fileContent(filename):
    'returns the content of file filename'
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    return content


# Here we define a function for reading the file
def fileLines(filename):
    'returns the content of file filename'
    infile = open(filename, 'r')
    fileLines = infile.readlines()
    infile.close()
    return fileLines
    # Here we define a function for reading the file


def fileLinesCount(filename):
    'returns the content of file filename'
    infile = open(filename, 'r')
    fileLines = infile.readlines()
    infile.close()
    return len(fileLines)


# Here we define a function for appending text to the file
def writeToFile(content, filename):
    'appends content to the filename'
    outfile = open(filename, 'a')
    outfile.write(content + '\n')
    outfile.close()
    return fileContent(filename);


# Here we ask the name of a file
print('Write product data into a file')
filename = input('Enter file name: ')
cont = 'y'
while str.lower(cont) != 'n':

    try:
        name = input('Enter name of product: ')
        price_str = input('Enter unit_price of product: ')
        amount_str = input('Enter amount of product: ')
        amount = eval(amount_str)
        price = eval(price_str)
        if amount<1 or price<0:
            raise ArithmeticError

    # Here we catch IOException
    except ArithmeticError as e:
        print('Price' + " or " + 'amount' + ' cannot be less than 1')

    else:
        outfile = open(filename, 'a')
        outfile.write(name + ';' + price_str + ';' + amount_str + '\n')
        outfile.close()
        print('Enter n to stop and y to continue: ')
        cont = input('do you want to continue? ')


print('Search for a product in the file')
filename = input('Enter the file name:')
search = 's'
while str.lower(search) != 'x':
    product = input('Enter name of product to be listed. ')
   # searchfile = open(filename,'r')
    infile = open(filename, 'r')
    contentList = infile.readlines()
    for line in contentList:
        if product in line:
            print(line)
            print('Enter s to continue search and x to exit')
            search = input('do you want to continue ')
infile.close()
