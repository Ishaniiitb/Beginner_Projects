#To generate the factorial of a number entered by the user

num = int(input("Enter the number whose factorial you want to generate : "))
pro = 1
for i in range(2, num+1):
    pro *= i
print("Factorial = ", pro)
