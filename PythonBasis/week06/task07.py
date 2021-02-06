class TotalResult:
    totalMarks = 0
    marksNumber = 0


def get_medium(total_result):
    if total_result.marksNumber == 0:
        return 0
    else:
        return total_result.totalMarks / total_result.marksNumber


def main():
    totals = [TotalResult(), TotalResult(), TotalResult()]

    inFile = open('input.txt', 'r', encoding='utf8')
    for line in inFile:
        splitted_line = line.strip().split()
        grade = int(splitted_line[2])
        mark = int(splitted_line[3])
        result = totals[grade - 9]
        result.totalMarks += mark
        result.marksNumber += 1
    inFile.close()

    print(get_medium(totals[0]), get_medium(totals[1]), get_medium(totals[2]))


main()
