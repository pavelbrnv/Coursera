n = int(input())

s = 0.0

while n > 0:
    s += 1 / (n ** 2)
    n -= 1

print(s)
