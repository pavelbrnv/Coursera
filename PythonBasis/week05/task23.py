minValue = 0
hasMinValue = False

for word in input().split():
    value = int(word)
    if value % 2 != 0 and (not hasMinValue or value < minValue):
        minValue = value
        hasMinValue = True

if hasMinValue:
    print(minValue)
