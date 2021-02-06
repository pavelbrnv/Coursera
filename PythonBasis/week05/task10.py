n = int(input())

previous = 1
result = 0
for i in range(1, n + 1):
    value = previous * i
    result += value
    previous = value

print(result)
