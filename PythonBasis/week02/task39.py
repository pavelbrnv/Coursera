current = 1
maximum = 0
maximumsCount = 0

while current != 0:
    current = int(input())
    if current != 0:
        if maximum == 0 or current > maximum:
            maximum = current
            maximumsCount = 1
        elif current == maximum:
            maximumsCount += 1

print(maximumsCount)
