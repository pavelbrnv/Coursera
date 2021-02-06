k = int(input())

i = 1
count = 0

while i <= k:
    inverted = 0
    temp = i
    while temp // 10 > 0:
        inverted += temp % 10
        inverted *= 10
        temp = temp // 10
    inverted += temp

    if i == inverted:
        count += 1

    i += 1

print(count)
