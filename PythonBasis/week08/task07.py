from itertools import accumulate

print(*accumulate(map(int, input().split()), lambda a, b: a + b))
