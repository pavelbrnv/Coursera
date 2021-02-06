words = input().split()

changes = 0
previousValue = int(words[0])

for word in words:
    value = int(word)
    if value != previousValue:
        changes += 1
    previousValue = value

print(changes + 1)
