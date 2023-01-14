sp = int(input("Enter the selling price : "))
cp = int(input("Enter the cost price : "))
if sp > cp:
    print("Profit")
    print(sp-cp)
elif cp > sp:
    print("Loss")
    print(cp-sp)
else:
    print("No profit no loss")

