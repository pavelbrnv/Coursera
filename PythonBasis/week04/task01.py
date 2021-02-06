def min4(a, b, c, d):
    m = min(a, b)
    m = min(m, c)
    m = min(m, d)
    return m


v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())

print(min4(v1, v2, v3, v4))
