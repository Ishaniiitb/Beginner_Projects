#To check if a number is a palindrome or not without using string functions

def reverse(n):
    rev = 0
    while n>0:
        d = n % 10
        rev = rev * 10 + d
        n //= 10
    return rev


num = int(input("Enter a number : "))
if num == reverse(num):
    print("Palindrome")
else:
    print("Not a palindrome")
