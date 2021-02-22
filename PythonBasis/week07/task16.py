candidates_votes = dict()

inFile = open('input.txt', 'r', encoding='utf8')
for state_votes in map(lambda p: p.split(), inFile):
    name = state_votes[0]
    votes = int(state_votes[1])
    candidate_votes = candidates_votes.get(name, 0)
    candidates_votes[name] = candidate_votes + votes
inFile.close()

for candidate in sorted(candidates_votes):
    print(candidate, candidates_votes[candidate])
