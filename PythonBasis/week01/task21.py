h = int(input())
a = int(input())
b = int(input())

aLessThanH = 0 ** (a // h)
aNotLessThanH = (aLessThanH + 1) % 2

result = aLessThanH * ((h - b - 1) // (a - b) + 1) + aNotLessThanH

print(result)
