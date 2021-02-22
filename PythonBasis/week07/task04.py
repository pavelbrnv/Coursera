values = map(int, input().split())
previous_values = set()
for value in values:
    if value in previous_values:
        print('YES')
    else:
        print('NO')
    previous_values.add(value)
