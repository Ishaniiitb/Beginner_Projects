#To generate the nth element of the fibonacci series using recursive functions

def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)


n = int(input("Enter which term of the fibonacci series you want : "))
print(fibo(n))

