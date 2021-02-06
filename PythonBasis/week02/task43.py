n = int(input())

while n // 10 > 0:
    v = n % 10
    print(v, end='')
    n = n // 10

print(n)
