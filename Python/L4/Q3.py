#To generate a^b using loops, a and b are inputs from the user

print("Enter the base and the exponent which you want to calcuate separated by a space : ")
base, expo = map(int, input().split())
pro = 1
for i in range(expo):
    pro *= base
print(f"{base}^{expo:2d} = {pro:2d}")

