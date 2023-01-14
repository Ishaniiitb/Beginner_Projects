#Code to genarate the nth Term of the fibonacci series
n = int(input("Enter which term of the fibonacci series you want : "))
a, b, c = 0, 1, 0
if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for i in range(2, n):
        c = a + b
        a, b = b, c
    print(c)

