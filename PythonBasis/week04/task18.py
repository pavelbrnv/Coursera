def C(n, k):
    if k == 0 or n == k:
        return 1
    elif k == 1:
        return n
    else:
        return C(n - 1, k) + C(n - 1, k - 1)


N = int(input())
K = int(input())

print(C(N, K))
