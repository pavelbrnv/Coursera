inFile = open('input.txt', 'r', encoding='utf8')

n = int(inFile.readline())

possible_answers = set(range(1, n + 1))

while True:
    line = inFile.readline().strip()
    if line == 'HELP':
        break

    values = set(map(int, line.split()))

    intersection = possible_answers & values
    difference = possible_answers - values

    if len(intersection) > len(difference):
        possible_answers = intersection
        print('YES')
    else:
        possible_answers = difference
        print('NO')

inFile.close()

print(*sorted(possible_answers))
