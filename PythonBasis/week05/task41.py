values = list(map(int, input().split()))

maxValue = 0
maxValueCount = 0

for value in values:
    valueCount = values.count(value)
    if valueCount > maxValueCount:
        maxValue = value
        maxValueCount = valueCount

print(maxValue)
