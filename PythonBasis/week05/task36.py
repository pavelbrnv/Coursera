values = list(map(int, input().split()))

pairsNumber = 0
for i in range(0, len(values) - 1):
    value = values[i]
    for j in range(i + 1, len(values)):
        if value == values[j]:
            pairsNumber += 1

print(pairsNumber)
