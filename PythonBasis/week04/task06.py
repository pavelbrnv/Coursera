def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def IsPointInCircle(x, y, xc, yc, r):
    return distance(x, y, xc, yc) <= r


X = float(input())
Y = float(input())
XC = float(input())
YC = float(input())
R = float(input())

if IsPointInCircle(X, Y, XC, YC, R):
    print('YES')
else:
    print('NO')
