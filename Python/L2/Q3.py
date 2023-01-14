print("Enter two numbers separated by a space : ")
a, b = map(int, input().split())
print(a,b)
temp = a
a = b
b = temp
print(a,b)
