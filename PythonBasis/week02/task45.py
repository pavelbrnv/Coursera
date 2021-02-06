previous = 0
current = 1
count = 0
maxCount = 0

while current != 0:
    current = int(input())
    if current != 0:
        if current == previous:
            count += 1
        else:
            previous = current
            if count > maxCount:
                maxCount = count
            count = 1

if count > maxCount:
    maxCount = count

print(maxCount)
