n = int(input())

r1 = n % 10
r2 = (n // 10) % 10
r3 = (n // 100) % 10
r4 = (n // 1000) % 10

diff1 = r1 - r4
diff2 = r2 - r3

absDiff1 = diff1 * diff1
absDiff2 = diff2 * diff2

diff = absDiff1 + absDiff2

result = 0 ** diff

print(result)
