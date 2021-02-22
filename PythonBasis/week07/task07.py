inFile = open('input.txt', 'r', encoding='utf8')

n = int(inFile.readline())

possible_answers = set()
not_answers = set()

while True:
    line = inFile.readline().strip()
    if line == 'HELP':
        break
    new_values = set(map(int, line.split()))

    line = inFile.readline().strip()
    if line == 'YES':
        if len(possible_answers) == 0:
            possible_answers = new_values
        else:
            possible_answers &= new_values
    elif line == 'NO':
        not_answers |= new_values

inFile.close()

if len(possible_answers) > 0:
    answers = sorted(possible_answers - not_answers)
    print(*answers)
else:
    for i in range(1, n + 1):
        if i not in not_answers:
            print(i, end=' ')
