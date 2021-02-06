def gcd(a, b):
    rem = a % b
    if rem == 0:
        return b
    else:
        return gcd(b, rem)


A = int(input())
B = int(input())

print(gcd(A, B))
