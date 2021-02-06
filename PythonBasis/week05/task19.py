def PrintNeighbors(numbers):
    if len(numbers) < 2:
        return

    for i in range(1, len(numbers)):
        if numbers[i - 1] * numbers[i] >= 0:
            print(numbers[i - 1], numbers[i])
            return


PrintNeighbors(list(map(int, input().split())))
