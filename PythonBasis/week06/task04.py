customerSize = int(input())
sizes = list(map(int, input().split()))

sizes.sort()

minSizesDiff = 3
previousSize = customerSize - minSizesDiff
pairsNumber = 0
for size in sizes:
    if size >= previousSize + minSizesDiff:
        pairsNumber += 1
        previousSize = size

print(pairsNumber)
