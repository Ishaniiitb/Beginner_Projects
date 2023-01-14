#To find the GCD of two numbers using recursive functions

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(a, a%b)


n1, n2 = map(int, input("Enter two numbers, whose GCD you want to find, separated by spaces : ").split())
print(gcd(max(n1,n2), min(n1,n2)))

