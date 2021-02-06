epsilon = 10 ** -6


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def isPointInCircle(x, y, xc, yc, r):
    return distance(x, y, xc, yc) < r


def isPointOnCircle(x, y, xc, yc, r):
    return abs(distance(x, y, xc, yc) - r) < epsilon


def isPointUnderLine(x, y, b, c):
    return y < b * x + c


def isPointAboveLine(x, y, b, c):
    return y > b * x + c


def isPointOnLine(x, y, b, c):
    return abs(y - (b * x + c)) < epsilon


def IsPointInArea(x, y):
    inCirc = isPointInCircle(x, y, -1, 1, 2)
    onCirc = isPointOnCircle(x, y, -1, 1, 2)
    under1 = isPointUnderLine(x, y, 2, 2)
    under2 = isPointUnderLine(x, y, -1, 0)
    above1 = isPointAboveLine(x, y, 2, 2)
    above2 = isPointAboveLine(x, y, -1, 0)
    on1 = isPointOnLine(x, y, 2, 2)
    on2 = isPointOnLine(x, y, -1, 0)
    inFirstArea = (inCirc or onCirc) and (above1 or on1) and (above2 or on2)
    inSecondArea = not inCirc and (under1 or on1) and (under2 or on2)
    return inFirstArea or inSecondArea


X = float(input())
Y = float(input())

if IsPointInArea(X, Y):
    print('YES')
else:
    print('NO')
