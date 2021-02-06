x = int(input())
y = int(input())

n = y - x + 1

if n == 1 or x % n == 1:
    print('YES')
else:
    print('NO')
