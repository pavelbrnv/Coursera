a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

epsilon = 10 ** -6

aIsZero = abs(a) < epsilon
bIsZero = abs(b) < epsilon
cIsZero = abs(c) < epsilon
dIsZero = abs(d) < epsilon
eIsZero = abs(e) < epsilon
fIsZero = abs(f) < epsilon

if aIsZero and bIsZero and not eIsZero:
    print(0)

elif cIsZero and dIsZero and not fIsZero:
    print(0)

elif aIsZero and bIsZero and eIsZero:
    if cIsZero and dIsZero and fIsZero:
        print(5)
    elif cIsZero:
        y = f / d
        print(4, y)
    elif dIsZero:
        x = f / c
        print(3, x)
    else:
        p = (-c) / d
        q = f / d
        print(1, p, q)

elif cIsZero and dIsZero and fIsZero:
    if aIsZero:
        y = e / b
        print(4, y)
    elif bIsZero:
        x = e / a
        print(3, x)
    else:
        p = (-a) / b
        q = e / b
        print(1, p, q)

elif aIsZero and cIsZero:
    y1 = e / b
    y2 = f / d
    if abs(y1 - y2) < epsilon:
        print(4, y1)
    else:
        print(0)

elif bIsZero and dIsZero:
    x1 = e / a
    x2 = f / c
    if abs(x1 - x2) < epsilon:
        print(3, x1)
    else:
        print(0)

elif aIsZero and dIsZero:
    x = f / c
    y = e / b
    print(2, x, y)

elif cIsZero and bIsZero:
    x = e / a
    y = f / d
    print(2, x, y)

elif aIsZero:
    y = e / b
    x = (f - d * y) / c
    print(2, x, y)

elif bIsZero:
    x = e / a
    y = (f - c * x) / d
    print(2, x, y)

elif cIsZero:
    y = f / d
    x = (e - b * y) / a
    print(2, x, y)

elif dIsZero:
    x = f / c
    y = (e - a * x) / b
    print(2, x, y)

elif abs(a * d - b * c) < epsilon:
    p1 = (-a) / b
    p2 = (-c) / d
    q1 = e / b
    q2 = f / d
    if abs(p1 - p2) < epsilon and abs(q1 - q2) < epsilon:
        print(1, p1, q1)
    else:
        print(0)

else:
    y = (a * f - c * e) / (a * d - b * c)
    x = (e - b * y) / a
    print(2, x, y)
