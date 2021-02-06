def getFullDeckSum(cardsNumber):
    deckSum = 0
    for cardNumber in range(1, cardsNumber + 1):
        deckSum += cardNumber
    return deckSum


n = int(input())
currentDeckSum = getFullDeckSum(n)

for i in range(0, n - 1):
    card = int(input())
    currentDeckSum -= card

print(currentDeckSum)
