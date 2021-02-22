class Party:
    a = 0
    b = 0


inFile = open('input.txt', 'r', encoding='utf8')
n, k = map(int, inFile.readline().split())
parties = []
for i in range(k):
    party = Party()
    party.a, party.b = map(int, inFile.readline().split())
    parties.append(party)
inFile.close()

counter = 0

for i in range(1, n + 1):
    if (i - 6) % 7 == 0 or i % 7 == 0:
        continue
    for party in parties:
        if i - party.a >= 0 and (i - party.a) % party.b == 0:
            counter += 1
            break

print(counter)
