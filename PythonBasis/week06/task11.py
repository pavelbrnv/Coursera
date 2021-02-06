max_marks = [0, 0, 0]

inFile = open('input.txt', 'r', encoding='utf8')
for line in inFile:
    splitted_line = line.strip().split()
    grade = int(splitted_line[2]) - 9
    mark = int(splitted_line[3])
    if max_marks[grade] < mark:
        max_marks[grade] = mark
inFile.close()

print(max_marks[0], max_marks[1], max_marks[2])
