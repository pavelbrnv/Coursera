def lagrange(n):
    sqrt = int(n ** 0.5)
    x1 = 0
    while x1 <= sqrt:
        x2 = 0
        while x2 <= x1:
            x3 = 0
            while x3 <= x2:
                x4 = 0
                while x4 <= x3:
                    if x1 * x1 + x2 * x2 + x3 * x3 + x4 * x4 == n:
                        return x1, x2, x3, x4
                    x4 += 1
                x3 += 1
            x2 += 1
        x1 += 1
    return 0, 0, 0, 0


N = int(input())
a, b, c, d = lagrange(N)
if a != 0:
    print(a, end=' ')
if b != 0:
    print(b, end=' ')
if c != 0:
    print(c, end=' ')
if d != 0:
    print(d, end=' ')
