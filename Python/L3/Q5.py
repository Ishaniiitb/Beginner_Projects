print("1) Addition \n2) Subtraction \n3) Division")
ch = int(input("Enter the operation which you want to perform : "))
print("Enter the numbers on which you want to perform the operation, separated by a space : ")
a, b = map(int, input().split())
if ch == 1:
    print(a+b)
elif ch == 2:
    print(a-b)
elif ch == 3:
    print(a/b)
else:
    print("Invalid choice entered")

