
def fileLength(filename):
    'returns the number of characters in file filename'
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    return 'The number of characters in ' + filename + ' is ' + str(len(content))
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
filename = input('Enter file name: ')
contentList = fileLines(filename)
print(contentList)

print('Number of prodcuts')
numberOfProducts = len(contentList)
print(numberOfProducts)
sum = 0
print('The total of each product: ')

for line in contentList:
    product = line.split(';')
    productTotal = eval(product[1])*eval(product[2])
    sum+=productTotal
    print(line.replace('\n', '') + ' product total: ' + str(productTotal))

print('The sum of all the product:')
print(sum,'Euros')

