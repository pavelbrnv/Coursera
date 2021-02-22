class Candidate:
    name = ''
    votes = 0


votes_number = 0
candidates = dict()

inFile = open('input.txt', 'r', encoding='utf8')
for name in map(lambda l: l.strip(), inFile):
    votes_number += 1
    candidate = candidates.get(name, Candidate())
    candidate.name = name
    candidate.votes += 1
    candidates[name] = candidate
inFile.close()

ordered_candidates = sorted(candidates.values(), key=lambda c: -c.votes)

outFile = open('output.txt', 'w', encoding='utf8')
winner = ordered_candidates[0]
print(winner.name, file=outFile)
if winner.votes <= votes_number / 2 and len(ordered_candidates) > 1:
    print(ordered_candidates[1].name, file=outFile)
outFile.close()
