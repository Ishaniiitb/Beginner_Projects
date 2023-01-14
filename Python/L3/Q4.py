print("Enter the three sides of a triangle separated by spaces : ")
s1, s2, s3 = map(int, input().split())
if s1 >= s2+s3 or s2 >= s1+s3 or s3 >= s1+s2:
    print("Invalid Triangle")
else:
    print("Valid Triangle")

