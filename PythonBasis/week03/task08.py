n = int(input())
x = float(input())

s = 0

i = 0
while i < n + 1:
    s *= x
    a = float(input())
    s += a
    i += 1

print(s)
