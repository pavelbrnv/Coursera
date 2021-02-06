def gcd(a, b):
    rem = a % b
    if rem == 0:
        return b
    else:
        return gcd(b, rem)


def ReduceFraction(n, m):
    d = gcd(n, m)
    return n // d, m // d


N = int(input())
M = int(input())

print(*ReduceFraction(N, M))
