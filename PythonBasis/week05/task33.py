values = list(map(int, input().split()))

minValue = values[0]
minIndex = 0
maxValue = values[0]
maxIndex = 0

for index in range(1, len(values)):
    value = values[index]
    if value < minValue:
        minValue = value
        minIndex = index
    if value > maxValue:
        maxValue = value
        maxIndex = index

values[minIndex], values[maxIndex] = values[maxIndex], values[minIndex]

print(*values)
