a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print(3)
        else:
            print(0)
    else:
        x = (-c) / b
        print(1, x)
else:
    d = (b * b) - (4 * a * c)
    if d < 0:
        print(0)
    elif d == 0.0:
        x = (-b) / (2 * a)
        print(1, x)
    elif d > 0:
        dSqrt = d ** 0.5
        x1 = (-b + dSqrt) / (2 * a)
        x2 = (-b - dSqrt) / (2 * a)
        if x1 > x2:
            print(2, x2, x1)
        else:
            print(2, x1, x2)
