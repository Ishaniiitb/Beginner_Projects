print("Enter the coordinates of three points, each x and y separated by a space : ")
x1, y1, x2, y2, x3, y3 = map(int, input().split())
area = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
if area == 0:
    print("Lie on the same straight line")
else:
    print("Don't lie on the same straight line")

