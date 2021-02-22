class Party:
    name = ''
    votes = 0
    places = 0
    remainder = 0.0


parties = []
total_votes = 0

inFile = open('input.txt', 'r', encoding='utf8')
for line in inFile:
    party = Party()
    splitting_index = line.rfind(' ')
    party.name = line[:splitting_index]
    party.votes = int(line[splitting_index:])
    parties.append(party)
    total_votes += party.votes
inFile.close()

quot = total_votes / 450
places_left = 450
for party in parties:
    full_places = party.votes / quot
    party.places = int(full_places)
    party.remainder = full_places - party.places
    places_left -= party.places

for party in sorted(parties, key=lambda p: (-p.remainder, -p.votes)):
    if places_left == 0:
        break
    party.places += 1
    places_left -= 1

for party in parties:
    print(party.name, party.places)
