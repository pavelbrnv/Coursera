def getNextIndex(values, currentIndex):
    nextIndex = currentIndex + 1
    if nextIndex < len(values):
        return nextIndex
    return -1


def merge(A, B):
    C = []
    ai, bi = 0, 0
    aValue, bValue = A[ai], B[bi]

    for i in range(len(A) + len(B)):
        if ai >= 0 and (bi < 0 or aValue < bValue):
            C.append(aValue)
            ai = getNextIndex(A, ai)
            if ai >= 0:
                aValue = A[ai]
        else:
            C.append(bValue)
            bi = getNextIndex(B, bi)
            if bi >= 0:
                bValue = B[bi]

    return C


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = merge(a, b)
print(*c)
