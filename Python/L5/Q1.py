#To generate the series 1+ x + x^2 + x^3 +...+ x^n, where 'x' and 'n' are inputs from the user

x, n = map(int, input("Enter the base and the max power separated by a space : ").split())
sum = 0
for i in range(n+1):
    print(f"{x:2d}^{i:2d} +", end="")
    sum += x**i
print(f"0 = {sum:2d}")

