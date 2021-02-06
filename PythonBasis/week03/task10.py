a = float(input())
b = float(input())
c = float(input())

d = (b * b) - (4 * a * c)

if d == 0.0:
    x = (-b) / (2 * a)
    print(x)
elif d > 0:
    dSqrt = d ** 0.5
    x1 = (-b + dSqrt) / (2 * a)
    x2 = (-b - dSqrt) / (2 * a)
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
