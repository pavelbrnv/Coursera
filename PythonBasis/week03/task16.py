s = input()

symbol = 'h'

firstIndex = s.find(symbol)
lastIndex = s.rfind(symbol)

result = s[:firstIndex] + s[lastIndex + 1:]

print(result)
