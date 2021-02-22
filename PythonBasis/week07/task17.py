inFile = open('input.txt', 'r', encoding='utf8')
words = inFile.read().split()
inFile.close()

words_counters = dict()
for word in words:
    counter = words_counters.get(word, 0)
    words_counters[word] = counter + 1

max_word_count = -1
max_word = ''
for word in words:
    count = words_counters[word]
    if count > max_word_count:
        max_word_count = count
        max_word = word
    elif count == max_word_count:
        max_word = min(word, max_word)

print(max_word)
