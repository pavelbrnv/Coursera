class Person:
    name = ''
    parent = None


persons = dict()

inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
for temp in range(n - 1):
    child_name, parent_name = inFile.readline().split()

    child = persons.get(child_name, None)
    if child is None:
        child = Person()
        child.name = child_name
        persons[child_name] = child

    parent = persons.get(parent_name, None)
    if parent is None:
        parent = Person()
        parent.name = parent_name
        persons[parent_name] = parent

    child.parent = parent
inFile.close()

for person in sorted(persons.values(), key=lambda p: p.name):
    level = 0
    parent = person.parent
    while parent is not None:
        level += 1
        parent = parent.parent
    print(person.name, level)
