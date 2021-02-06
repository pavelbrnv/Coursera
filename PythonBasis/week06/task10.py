n = int(input())
keys_limits = list(map(int, input().split()))

k = int(input())
for key_index in map(lambda p: int(p) - 1, input().split()):
    keys_limits[key_index] -= 1

for key_limit in keys_limits:
    if key_limit >= 0:
        print('NO')
    else:
        print('YES')
