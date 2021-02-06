maxValue = 0
maxValueIndex = -1
index = -1

for word in input().split():
    value = int(word)
    index += 1
    if maxValueIndex < 0 or value > maxValue:
        maxValue = value
        maxValueIndex = index

print(maxValue, maxValueIndex)
