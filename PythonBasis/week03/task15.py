s = input()

symbol = 'f'

firstIndex = s.find(symbol)

if firstIndex >= 0:
    print(firstIndex)

    lastIndex = s.rfind(symbol)
    if lastIndex != firstIndex:
        print(lastIndex)
