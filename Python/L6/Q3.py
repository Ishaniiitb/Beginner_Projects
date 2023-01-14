#To generate the HCF(higest common factor) of two numbers enetered by the user.

def hcf(n1, n2):
    max = 1
    for i in range(2, min(n1, n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            max = i
    return max


a, b = map(int, input("Enter two numbers separated by a space to know their highest common factor : ").split())
print(hcf(a,b))

