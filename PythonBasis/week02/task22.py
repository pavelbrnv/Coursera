k = int(input())
m = int(input())
n = int(input())

if n > k:
    rounds = (n * 2) // k
    if (n * 2) % k != 0:
        rounds += 1
else:
    rounds = 2

print(m * rounds)
