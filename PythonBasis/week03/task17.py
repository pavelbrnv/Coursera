s = input()

symbol = 'h'

firstIndex = s.find(symbol)
lastIndex = s.rfind(symbol)

subLen = lastIndex - firstIndex - 1

if subLen > 0:
    sub = s[firstIndex + 1:lastIndex]
else:
    sub = ''

result = s[:firstIndex + 1] + sub + sub + s[lastIndex:]
print(result)
