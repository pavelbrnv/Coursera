s = input()

symbol = ' '

index = s.find(symbol)

first = s[:index]
second = s[index + 1:]

result = second + symbol + first
print(result)
