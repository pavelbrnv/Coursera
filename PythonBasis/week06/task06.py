def getNumber(value):
    return value[0]


def getDistance(value):
    return value[1]


def getNearestShelterIndex(village, startingShelterIndex):
    previousDistance = -1
    for index in range(startingShelterIndex, len(shelters)):
        shelter = shelters[index]
        distance = abs(shelter[1] - village[1])
        if 0 <= previousDistance < distance:
            return index - 1
        previousDistance = distance
    return index


n = int(input())
villages = []
villageNumber = 0
for distance in input().split():
    villageNumber += 1
    villages.append([villageNumber, int(distance), 0])

m = int(input())
shelters = []
shelterNumber = 0
for distance in input().split():
    shelterNumber += 1
    shelters.append((shelterNumber, int(distance)))

villages.sort(key=getDistance)
shelters.sort(key=getDistance)

shelterIndex = 0
for village in villages:
    shelterIndex = getNearestShelterIndex(village, shelterIndex)
    shelter = shelters[shelterIndex]
    village[2] = shelter[0]

villages.sort(key=getNumber)


def getShelterNumberText(villgae):
    return str(villgae[2])


result = ' '.join(map(getShelterNumberText, villages))
print(result)
