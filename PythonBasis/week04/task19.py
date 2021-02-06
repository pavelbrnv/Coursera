def getRecursionSum(s):
    n = int(input())
    if n == 0:
        return s
    return getRecursionSum(s + n)


print(getRecursionSum(0))
