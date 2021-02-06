def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    return a * power(a, n - 1)


A = float(input())
N = int(input())

print(power(A, N))
