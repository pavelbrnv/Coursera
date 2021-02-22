inFile = open('input.txt', 'r', encoding='utf8')

synonims = dict()

n = int(inFile.readline().strip())
for temp in range(n):
    word1, word2 = inFile.readline().split()
    synonims[word1] = word2
    synonims[word2] = word1

word = inFile.readline().strip()
print(synonims[word])

inFile.close()
