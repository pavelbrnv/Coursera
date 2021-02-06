a = int(input())
b = int(input())

aImage = (a // b) * b

medium = (a + aImage) // 2 + (a + aImage) % 2

aFlag = a // medium
aImageFlag = aImage // medium
aEqualityFlag = aFlag * aImageFlag
aDifferenceFlag = (aEqualityFlag + 1) % 2

print('YES' * aEqualityFlag + 'NO' * aDifferenceFlag)
