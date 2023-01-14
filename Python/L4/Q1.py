#To generate a multiplication table of a number entered by the user

num = int(input("Enter the number whose multiplication table you want to generate : "))
for i in range(11):
    pro = num * i
    print(f"{num} * {i:3d} = {pro:3d}")

