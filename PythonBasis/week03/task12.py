a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a == 0.0:
    y = e / b
    x = (f - d * y) / c
elif b == 0.0:
    x = e / a
    y = (f - c * x) / d
elif c == 0.0:
    y = f / d
    x = (e - b * y) / a
elif d == 0.0:
    x = f / c
    y = (e - a * x) / b
else:
    y = (a * f - c * e) / (a * d - b * c)
    x = (e - b * y) / a

print(x, y)
