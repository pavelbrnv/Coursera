values = list(map(int, input().split()))

checkingIndexes = list(range(0, len(values)))
for i in range(0, len(checkingIndexes)):
    index = checkingIndexes[i]
    if index < 0:
        continue

    value = values[index]

    valueIsUnique = True
    for k in range(index + 1, len(values)):
        if value == values[k]:
            checkingIndexes[k] = -1
            valueIsUnique = False

    if valueIsUnique:
        print(value, end=' ')
