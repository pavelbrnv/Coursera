positives = 0
for word in input().split():
    if int(word) > 0:
        positives += 1
print(positives)
