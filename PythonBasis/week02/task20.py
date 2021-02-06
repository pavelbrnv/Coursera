k = int(input())

condition1 = k % 3 == 0
condition2 = k >= 5 and (k - 5) % 3 == 0
condition3 = k >= 10 and (k - 10) % 3 == 0

if condition1 or condition2 or condition3:
    print('YES')
else:
    print('NO')
