a = int(input())
b = int(input())

if a < b:
    r = range(a, b + 1)
else:
    r = range(a, b - 1, -1)

for i in r:
    print(i, end=' ')
