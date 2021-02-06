def power(a, n):
    p = 1
    while n > 0:
        p *= a
        n -= 1
    while n < 0:
        p /= a
        n += 1
    return p


A = float(input())
N = int(input())

print(power(A, N))
