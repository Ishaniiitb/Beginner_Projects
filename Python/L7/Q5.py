#To calculate a^b using recursive functions

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)


base, expo = map(int, input("Enter the base and exponent separated by a space respectively : ").split())
print(power(base,expo))

