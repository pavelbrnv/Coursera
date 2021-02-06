def revert():
    n = int(input())
    if n > 0:
        revert()
    print(n)


revert()
