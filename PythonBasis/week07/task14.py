inFile = open('input.txt', 'r', encoding='utf8')
words = inFile.read().split()
inFile.close()

words_counters = dict()
for word in words:
    counter = words_counters.get(word, 0)
    print(counter, end=' ')
    words_counters[word] = counter + 1
