def UpdateIncreasingValuesByMaximumIfNeed(values, maximum):
    for i in range(0, len(values)):
        if maximum <= values[i]:
            return

        if i + 1 < len(values) and values[i + 1] < maximum:
            values[i] = values[i + 1]
        else:
            values[i] = maximum


def UpdateIncreasingValuesByMinimumIfNeed(values, minimum):
    for i in range(len(values) - 1, -1, -1):
        if values[i] <= minimum:
            return

        if i - 1 >= 0 and minimum < values[i - 1]:
            values[i] = values[i - 1]
        else:
            values[i] = minimum


allValues = list(map(int, input().split()))
initMin = min(allValues[0], allValues[1], allValues[2])
initMax = max(allValues[0], allValues[1], allValues[2])
initMed = (allValues[0] + allValues[1] + allValues[2]) - initMin - initMax

maximums = [initMin, initMed, initMax]
minimums = [initMin, initMed, initMax]

for j in range(3, len(allValues)):
    UpdateIncreasingValuesByMaximumIfNeed(maximums, allValues[j])
    UpdateIncreasingValuesByMinimumIfNeed(minimums, allValues[j])

maxMul = maximums[0] * maximums[1] * maximums[2]
minMaxMul = minimums[0] * minimums[1] * maximums[2]

if maxMul > minMaxMul:
    print(*maximums)
else:
    print(minimums[0], minimums[1], maximums[2])
