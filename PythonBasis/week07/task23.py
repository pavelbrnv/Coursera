dictionary = dict()

inFile = open('input.txt', 'r', encoding='utf8')

n = int(inFile.readline())

for temp in range(n):
    word = inFile.readline().strip()
    lower_word = word.lower()
    variants = dictionary.get(lower_word, None)
    if variants is None:
        variants = set()
        dictionary[lower_word] = variants
    variants.add(word)

text_words = inFile.readline().split()

inFile.close()

mistakes_number = 0

for word in text_words:
    variants = dictionary.get(word.lower(), None)
    if variants is None:
        upper_letters_number = 0
        for letter in word:
            if letter.isupper():
                upper_letters_number += 1
        if upper_letters_number != 1:
            mistakes_number += 1
    else:
        if word not in variants:
            mistakes_number += 1

print(mistakes_number)
