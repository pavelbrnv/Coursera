grades_marks = [[], [], []]

inFile = open('input.txt', 'r', encoding='utf8')
for line in inFile:
    splitted_line = line.strip().split()
    grade = int(splitted_line[2]) - 9
    mark = int(splitted_line[3])
    grades_marks[grade].append(mark)
inFile.close()

for grade_marks in grades_marks:
    grade_marks.sort(reverse=True)
    winner_mark = grade_marks[0]
    winners_number = 0
    for mark in grade_marks:
        if mark == winner_mark:
            winners_number += 1
        else:
            break
    print(winners_number, end=' ')
