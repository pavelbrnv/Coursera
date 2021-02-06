def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


X = float(input())
Y = float(input())

if IsPointInSquare(X, Y):
    print('YES')
else:
    print('NO')
