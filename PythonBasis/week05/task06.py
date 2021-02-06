n = int(input())

zeros = 0
for i in range(0, n):
    x = int(input())
    if x == 0:
        zeros += 1

print(zeros)
