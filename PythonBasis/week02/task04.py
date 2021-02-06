v = int(input())

if v % 400 == 0:
    print('YES')
elif v % 100 == 0:
    print('NO')
elif v % 4 == 0:
    print('YES')
else:
    print('NO')
