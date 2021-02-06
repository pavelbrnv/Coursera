def IsPrime(n):
    divisor = 2
    limit = int(n ** 0.5)

    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += 1

    return True


N = int(input())
if IsPrime(N):
    print('YES')
else:
    print('NO')
