current = 1
maximum = 0
secondMaximum = 0

while current != 0:
    current = int(input())
    if current != 0:
        if maximum == 0 or current >= maximum:
            secondMaximum = maximum
            maximum = current
        elif secondMaximum == 0 or current > secondMaximum:
            secondMaximum = current

print(secondMaximum)
