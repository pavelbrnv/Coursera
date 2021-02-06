def MinDivisor(n):
    divisor = 2
    limit = int(n ** 0.5)

    while divisor <= limit:
        if n % divisor == 0:
            return divisor
        divisor += 1

    return n


N = int(input())
print(MinDivisor(N))
