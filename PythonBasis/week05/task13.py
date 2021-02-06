index = 0
for word in input().split():
    if index % 2 == 0:
        print(word, end=' ')
    index += 1
