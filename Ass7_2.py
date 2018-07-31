
def sum_series(n):
    for i in range(1, n):
        return 1/(3*i + 2) + sum_series(n)


print(sum_series(3))