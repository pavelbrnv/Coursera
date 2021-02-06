def fastPow(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        return fastPow(a * a, n // 2)
    else:
        return a * fastPow(a, n - 1)


A = float(input())
N = int(input())

print(fastPow(A, N))
