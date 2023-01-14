def factorial(n):
    pro = 1
    for i in range(2, n+1):
        pro *= i
    return pro


def nCr(n, r):
    coeff = factorial(n) // (factorial(r) * factorial(n-r))
    return coeff


n = int(input("Enter the number of rows of Pascals triangle you want to generate : "))
spaces = 3*(n-1)
for i in range(n):
    print(" "*spaces, end="")
    for j in range(i+1):
        print(f"{nCr(i,j):6d}", end="")
    print()
    spaces -= 3

