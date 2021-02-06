def CountSort(A):
    counter = [0] * 101
    for i in A:
        counter[i] += 1

    index = 0
    for value in range(len(counter)):
        for i in range(counter[value]):
            A[index] = value
            index += 1

    return A


def main():
    values = list(map(int, input().split()))
    CountSort(values)
    print(*values)


main()
