class PersonMark:
    surname = ''
    name = ''
    school_number = 0
    mark = 0


def main():
    marks = []

    inFile = open('input.txt', 'r', encoding='utf8')
    for line in inFile:
        splitted_line = line.strip().split()
        mark = PersonMark()
        mark.surname = splitted_line[0]
        mark.name = splitted_line[1]
        mark.school_number = int(splitted_line[2])
        mark.mark = int(splitted_line[3])
        marks.append(mark)
    inFile.close()

    marks.sort(key=lambda p: (p.surname, p.name, p.mark))

    outFile = open('output.txt', 'w', encoding='utf8')
    for mark in marks:
        print(mark.surname, mark.name, mark.mark, file=outFile)
    outFile.close()


main()
