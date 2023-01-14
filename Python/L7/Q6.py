#To check if a number is a palindrome or not using recursive functions

def reverse(n,l):
    if 0 <= n <= 9:
        return n
    else:
        return (n%10) * pow(10,l) + reverse(n//10, l-1)


num = input("Enter a number : ")
if int(num) == reverse(int(num), len(num)-1):
    print("Palindrome")
else:
    print("Not a palindrome")

