def split(n, terms):
    limit = int(n ** (1 / 3))
    x = limit
    while x > 0:
        x3 = x * x * x
        diff = n - x3
        if diff > 0:
            if terms > 1:
                diffSplit = split(diff, terms - 1)
                if len(diffSplit) > 0:
                    return str(x3) + ' ' + diffSplit
        elif diff == 0:
            return str(x3) + ' '
        else:
            return ''
        x -= 1
    return ''


N = int(input())
result = split(N, 7)
if len(result) > 0:
    print(result)
else:
    print(0)
