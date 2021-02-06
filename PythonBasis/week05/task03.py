n = int(input())

start = 10 ** (n - 1)
end = 10 ** n

for i in range(end - 1, start - 1, -2):
    print(i, end=' ')
