def Intersection(A, B):
    C = []

    ai, bi = 0, 0
    while ai < len(A) and bi < len(B):
        aValue, bValue = A[ai], B[bi]
        if aValue < bValue:
            ai += 1
        elif bValue < aValue:
            bi += 1
        else:
            C.append(aValue)
            ai += 1
            bi += 1

    return C


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = Intersection(a, b)
print(*c)
