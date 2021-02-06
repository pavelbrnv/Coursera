def IsAscending(A):
    if len(A) < 2:
        return True

    i = 1
    while i < len(A) and A[i] > A[i - 1]:
        i += 1
    return i == len(A)


numbers = list(map(int, input().split()))
result = IsAscending(numbers)
if result:
    print('YES')
else:
    print('NO')
