p2 = -1
p1 = -1
p0 = -1
p0Index = 0
previousMaximumIndex = 0
minOffset = 0

while p0 != 0:
    p2 = p1
    p1 = p0
    p0 = int(input())
    p0Index += 1

    if 0 < p2 < p1 and 0 < p0 < p1:
        maximumIndex = p0Index - 1
        if previousMaximumIndex > 0:
            offset = maximumIndex - previousMaximumIndex
            if offset < minOffset or minOffset == 0:
                minOffset = offset
        previousMaximumIndex = maximumIndex

print(minOffset)
