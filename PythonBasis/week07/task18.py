inFile = open('input.txt', 'r', encoding='utf8')
words = inFile.read().split()
inFile.close()

words_counters = dict()
for word in words:
    counter = words_counters.get(word, 0)
    words_counters[word] = counter + 1

for i in sorted(words_counters.items(), key=lambda p: (-int(p[1]), p[0])):
    print(i[0])
