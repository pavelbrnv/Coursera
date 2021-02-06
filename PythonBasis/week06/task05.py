s, n = map(int, input().split())

sizes = []
for i in range(n):
    size = int(input())
    sizes.append(size)

sizes.sort()

fullSize = 0
counter = 0
for size in sizes:
    fullSize += size
    if fullSize > s:
        break
    counter += 1

print(counter)
