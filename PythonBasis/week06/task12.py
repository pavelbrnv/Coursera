class Person:
    surname = ''
    mark = 0


n = int(input())
persons = []
for i in range(n):
    line = input().split()
    person = Person()
    person.surname = line[0]
    person.mark = int(line[1])
    persons.append(person)

persons.sort(key=lambda p: p.mark, reverse=True)

for person in persons:
    print(person.surname)
