def IsPointInSquare(x, y):
    return -1 <= abs(x) + abs(y) <= 1


X = float(input())
Y = float(input())

if IsPointInSquare(X, Y):
    print('YES')
else:
    print('NO')
