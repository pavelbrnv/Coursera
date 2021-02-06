n = int(input())

high = n // 10
low = n % 10

if low == 0 or 5 <= low <= 9 or high == 1:
    print(n, 'korov')
elif low == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
