def GetNextNotZeroIndex(numbers, index):
    for i in range(index + 1, len(numbers)):
        if numbers[i] != 0:
            return i
    return -1


def CompressList(numbers):
    j = 0
    for i in range(len(numbers)):
        if values[i] == 0:
            j = GetNextNotZeroIndex(values, max(i, j))
            if j < 0:
                return
            values[i], values[j] = values[j], values[i]


values = list(map(int, input().split()))
CompressList(values)
print(*values)
