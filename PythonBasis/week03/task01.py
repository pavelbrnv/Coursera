a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2

s2 = p * (p - a) * (p - b) * (p - c)
s = s2 ** 0.5

print(s)
