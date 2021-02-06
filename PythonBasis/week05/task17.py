hasPrevious = False
previous = 0

for word in input().split():
    value = int(word)
    if hasPrevious and value > previous:
        print(value, end=' ')
    hasPrevious = True
    previous = value
