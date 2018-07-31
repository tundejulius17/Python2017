print('Enter n greater than 1\n')
n = eval(input(':'))
print('Enter m greater than 1\n')
m = eval(input(':'))
def sum_values(n, m):
    #sum = 0
    if n == m:
        return n

    return n + sum_values(n+1,m)

print(str(sum_values(n,m)))

#print(str(sum_values(2,100)))
