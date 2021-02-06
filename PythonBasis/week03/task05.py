import math

x = float(input())

integer = math.floor(x)
remainder = x - integer

if remainder >= 0.5:
    rounded = integer + 1
else:
    rounded = integer

print(rounded)
