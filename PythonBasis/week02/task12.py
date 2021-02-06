x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

xDiff = x2 - x1
yDiff = y2 - y1

if yDiff > 0 and -yDiff <= xDiff <= yDiff and (x1 + y1) % 2 == (x2 + y2) % 2:
    print('YES')
else:
    print('NO')
