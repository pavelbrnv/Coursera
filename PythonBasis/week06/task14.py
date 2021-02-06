marks_number = 3
good_mark_lower_bound = 40


class Student:
    total_mark = 0


class EqualityGroup:
    total_mark = 0
    students_number = 0


def main():
    k = -1
    students = []

    inFile = open('input.txt', 'r', encoding='utf8')
    for line in inFile:
        if k < 0:
            k = int(line.strip())
        else:
            line = line.strip().split()
            student = Student()
            student_is_good = True
            for i in range(len(line) - 1, len(line) - 1 - marks_number, -1):
                mark = int(line[i])
                if mark < good_mark_lower_bound:
                    student_is_good = False
                    break
                else:
                    student.total_mark += mark
            if student_is_good:
                students.append(student)
    inFile.close()

    students.sort(key=lambda s: s.total_mark, reverse=True)

    groups = []
    for student in students:
        if len(groups) > 0 \
                and student.total_mark == groups[-1].total_mark:
            groups[-1].students_number += 1
        else:
            group = EqualityGroup()
            group.total_mark = student.total_mark
            group.students_number = 1
            groups.append(group)

    total_students_number = 0
    last_group_index = -1
    for group in groups:
        if total_students_number + group.students_number > k:
            break
        total_students_number += group.students_number
        last_group_index += 1

    outFile = open('output.txt', 'w', encoding='utf8')
    if last_group_index == len(groups) - 1:
        print(0, file=outFile)
    elif last_group_index < 0:
        print(1, file=outFile)
    else:
        print(groups[last_group_index].total_mark, file=outFile)
    outFile.close()


main()
