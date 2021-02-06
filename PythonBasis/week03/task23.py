s = input()

symbol = 'h'
symbolReplaced = 'H'

first = s.find(symbol)
last = s.rfind(symbol)

subLen = last - first - 1

if subLen > 0:
    sub = s[first + 1:last]
else:
    sub = ''

result = s[:first + 1] + sub.replace(symbol, symbolReplaced) + s[last:]
print(result)
