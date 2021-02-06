s = input()

symbol = 'f'

firstIndex = s.find(symbol)
if firstIndex >= 0:
    secondIndex = s.find(symbol, firstIndex + 1)
    print(secondIndex)
else:
    print(-2)
