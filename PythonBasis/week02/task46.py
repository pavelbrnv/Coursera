previous = 0
current = 1
count = 0
maxCount = 0
trend = 0

while current != 0:
    current = int(input())

    if current != 0:
        oldTrend = trend

        if previous == 0 or current == previous:
            trend = 0
        elif current > previous:
            trend = 1
        else:
            trend = -1

        if trend == 0:
            if count > maxCount:
                maxCount = count
            count = 1
        elif trend != oldTrend:
            if count > maxCount:
                maxCount = count
            count = 2
        else:
            count += 1

        previous = current

if count > maxCount:
    maxCount = count

print(maxCount)
