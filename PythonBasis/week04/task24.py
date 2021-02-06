def getSquares():
    n = int(input())
    if n == 0:
        return ''

    subSquares = getSquares()

    nSqrt = int(n ** 0.5)
    if nSqrt * nSqrt == n:
        subSquares += str(n) + ' '

    return subSquares


squares = getSquares()
if len(squares) == 0:
    print(0)
else:
    print(squares)
