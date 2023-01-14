"""To check if two numbers, input by the user, are twin prime numbers or not. Twin prime numbers are two numbers such that both numbers are prime and their difference is 2
"""

def prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


a, b = map(int, input("Enter two numbers separated by a space : ").split())
if prime(a) and prime(b) and abs(a-b) == 2:
    print("Twin Prime Numbers")
else:
    print("Not twin prime numbers")

