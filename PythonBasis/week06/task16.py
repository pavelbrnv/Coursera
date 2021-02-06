def sort_and_print_second(grade_marks):
    if len(grade_marks) == 0:
        print(0)
        return

    grade_marks.sort(reverse=True)

    winner_mark = grade_marks[0]
    for grade_mark in grade_marks:
        if grade_mark != winner_mark:
            print(grade_mark, end=' ')
            return

    print(0)


marks = [[], [], []]

inFile = open('input.txt', 'r', encoding='utf8')
for line in inFile:
    splitted_line = line.strip().split()
    grade = int(splitted_line[2]) - 9
    mark = int(splitted_line[3])
    marks[grade].append(mark)
inFile.close()

sort_and_print_second(marks[0])
sort_and_print_second(marks[1])
sort_and_print_second(marks[2])
