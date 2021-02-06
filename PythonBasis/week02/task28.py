n = int(input())

val = 1
isPower = False

while val <= n:
    if val == n:
        isPower = True
    val = val * 2

if isPower:
    print('YES')
else:
    print('NO')
