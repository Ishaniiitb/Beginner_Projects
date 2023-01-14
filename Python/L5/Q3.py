""" To generate a square matrix, if the user enters n = 2, then the matrix should be:-
1 2
3 4
"""

n = int(input("Enter the number of rows you want in your square matrix : "))
c = 1
for i in range(n):
    for j in range(n):
        print(f"{c:3d}", end = "")
        c += 1
    print()

