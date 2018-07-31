
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

matrixAddition = [[0, 0, 0],[0,0,0],[0,0,0]]

matrixSubtraction = [[0, 0, 0],[0,0,0],[0,0,0]]

# iterate through rows
print("Matrix addition")
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       matrixAddition[i][j] = X[i][j] + Y[i][j]

for r in matrixAddition:
   print(r)

print()

print("Matrix subtraction")
for i in range(len(X)):
    for j in range(len(X[0])):
        matrixSubtraction[i][j] = X[i][j] - Y[i][j]

for r in matrixSubtraction:
    print(r)

print()

matrix1 = [[12,7,3], [4 ,5,6], [7 ,8,9]]
# 3x4 matrix
matrix2 = [[5,8,1,2], [6,7,3,0],[4,5,9,1]]
# result is 3x4
matrixMutiplication = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# iterate through rows of X
print("Matrix multiplication")
for i in range(len(matrix1)):
   # iterate through columns of Y
   for j in range(len(matrix2[0])):
       # iterate through rows of Y
       for k in range(len(matrix2)):
           matrixMutiplication[i][j] += matrix1[i][k] * matrix2[k][j]

for r in matrixMutiplication:
   print(r)