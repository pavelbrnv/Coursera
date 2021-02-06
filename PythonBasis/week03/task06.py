import math

p = int(input())
x = int(input())
y = int(input())

deposit = x * 100 + y
income = math.floor(deposit * (p / 100))
result = deposit + income

resultRuble = result // 100
resultPenny = result % 100

print(resultRuble, resultPenny)
