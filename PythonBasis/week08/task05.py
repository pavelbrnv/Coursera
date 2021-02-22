from functools import reduce

print(reduce(lambda a, b: a * b, map(lambda x: int(x)**5, input().split())))
