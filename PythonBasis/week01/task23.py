a = int(input())
b = int(input())

medium = (a + b) // 2 + (a + b) % 2

aFlag = a // medium
bFlag = b // medium
equalityFlag = aFlag * bFlag
differenceFlag = (equalityFlag + 1) % 2

result = equalityFlag * a + differenceFlag * (a * aFlag + b * bFlag)

print(result)
