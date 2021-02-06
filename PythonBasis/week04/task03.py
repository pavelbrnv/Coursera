def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())
X3 = float(input())
Y3 = float(input())

p = distance(X1, Y1, X2, Y2)
p += distance(X2, Y2, X3, Y3)
p += distance(X3, Y3, X1, Y1)
print(p)
