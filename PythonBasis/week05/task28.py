n = input()
values = list(map(int, input().split()))
x = int(input())

closest = values[0]
delta = abs(closest - x)

if len(values) > 1:
    for i in range(1, len(values)):
        currentDelta = abs(values[i] - x)
        if currentDelta < delta:
            closest = values[i]
            delta = currentDelta

print(closest)
