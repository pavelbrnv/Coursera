def CountGreaterNeighbors(numbers):
    count = 0
    if len(numbers) > 2:
        for i in range(1, len(numbers) - 1):
            if numbers[i - 1] < numbers[i] and numbers[i + 1] < numbers[i]:
                count += 1
    return count


result = CountGreaterNeighbors(list(map(int, input().split())))
print(result)
