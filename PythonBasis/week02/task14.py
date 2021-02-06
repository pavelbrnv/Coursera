a = int(input())
b = int(input())
c = int(input())

aRem = a % 2
bRem = b % 2
cRem = c % 2

if aRem != bRem or aRem != cRem or bRem != cRem:
    print('YES')
else:
    print('NO')
