def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)


A = int(input())
B = int(input())

print(sum(A, B))
