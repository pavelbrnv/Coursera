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


def MultiplyValues(values):
    result = 1
    for value in values:
        result *= value
    return result


allValues = list(map(int, input().split()))
initialMin = min(allValues[0], allValues[1])
initialMax = max(allValues[0], allValues[1])
maximums = [initialMin, initialMax]
minimums = [initialMin, initialMax]

for j in range(2, len(allValues)):
    UpdateIncreasingValuesByMaximumIfNeed(maximums, allValues[j])
    UpdateIncreasingValuesByMinimumIfNeed(minimums, allValues[j])

if MultiplyValues(maximums) > MultiplyValues(minimums):
    print(*maximums)
else:
    print(*minimums)
