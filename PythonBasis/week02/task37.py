current = 1
previous = 0
counter = 0

while current != 0:
    current = int(input())
    if current != 0 and previous != 0 and current > previous:
        counter += 1
    previous = current

print(counter)
