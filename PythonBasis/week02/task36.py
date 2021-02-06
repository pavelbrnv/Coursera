counter = 0
current = 1

while current != 0:
    current = int(input())
    if current != 0 and current % 2 == 0:
        counter += 1

print(counter)
