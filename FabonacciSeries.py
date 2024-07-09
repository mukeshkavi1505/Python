def fabonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fabonacci(n - 1) + fabonacci(n - 2)
def printFabonacciSeries(n):
    for i in range(n):
        print(fabonacci(i), end=' ')

print("Fibonacci series up to 6th term:")
printFabonacciSeries(6)
print()
print("6th term of Fibonacci series:", fabonacci(6))
