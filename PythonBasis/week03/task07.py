import math

p = int(input())
x = int(input())
y = int(input())
k = int(input())

ruble = x
penny = y

i = 0
while i < k:
    deposit = ruble * 100 + penny
    income = math.floor(deposit * (p / 100))
    result = deposit + income

    ruble = result // 100
    penny = result % 100

    i += 1

print(ruble, penny)
