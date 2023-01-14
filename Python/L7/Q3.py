#To find the sum of digits in a number using recursive functions

def summation(n):
    if 0 <= n <= 9:
        return n
    else:
        return (n%10) + summation(n//10)


num = int(input("Enter a number : "))
print(summation(num))

