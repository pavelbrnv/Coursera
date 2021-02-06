schools = [0] * 99

inFile = open('input.txt', 'r', encoding='utf8')
for line in inFile:
    splitted_line = line.strip().split()
    school = int(splitted_line[2])
    schools[school - 1] += 1
inFile.close()

max_number = -1
max_number_indexes = []

for i in range(len(schools)):
    number = schools[i]
    if number > max_number:
        max_number = number
        max_number_indexes.clear()
        max_number_indexes.append(i + 1)
    elif number == max_number:
        max_number_indexes.append(i + 1)

print(*max_number_indexes)
