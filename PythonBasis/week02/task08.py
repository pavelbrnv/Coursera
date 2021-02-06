n = int(input())
m = int(input())
k = int(input())

nDirection = k // n < m and k % n == 0
mDirection = k // m < n and k % m == 0

if nDirection or mDirection:
    print('YES')
else:
    print('NO')
