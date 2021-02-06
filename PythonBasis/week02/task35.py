current = 1
total = 0
counter = 0

while current != 0:
    current = int(input())
    total += current
    counter += 1

counter -= 1

if counter == 0:
    average = 0
else:
    average = total / counter

print(average)
