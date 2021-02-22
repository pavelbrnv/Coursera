inFile = open('input.txt', 'r', encoding='utf8')

n = int(inFile.readline().strip())
cities = dict()

for temp in range(n):
    names = inFile.readline().split()
    country = names[0]
    for i in range(1, len(names)):
        city = names[i]
        cities[city] = country

m = int(inFile.readline().strip())

for temp in range(m):
    city = inFile.readline().strip()
    print(cities[city])

inFile.close()
