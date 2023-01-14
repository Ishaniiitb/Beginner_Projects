#To calculate the factorial of a number using recursive functions

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


num = int(input("Enter the number whose factorial you want to find : "))
print("Factorial of the number is", factorial(num))

