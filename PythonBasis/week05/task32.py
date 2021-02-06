words = input().split()

last = words[-1]
for i in range(len(words) - 1, 0, -1):
    words[i] = words[i - 1]
words[0] = last

print(*words)
