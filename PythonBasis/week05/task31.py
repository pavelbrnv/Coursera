words = input().split()

for i in range(1, len(words), 2):
    words[i - 1], words[i] = words[i], words[i - 1]

print(*words)
