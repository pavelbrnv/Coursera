aX = int(input())
aY = int(input())
bX = int(input())
bY = int(input())

aIsEven = (aX + aY) % 2 == 0
bIsEven = (bX + bY) % 2 == 0

if aIsEven == bIsEven:
    print('YES')
else:
    print('NO')
