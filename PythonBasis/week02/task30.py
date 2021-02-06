x = int(input())
y = int(input())

current = x
days = 1

while current < y:
    current *= 1.1
    days += 1

print(days)
