values = input().split()
x = int(input())

tallerCounter = 0
for value in values:
    height = int(value)
    if height >= x:
        tallerCounter += 1

print(tallerCounter + 1)
