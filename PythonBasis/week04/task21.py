def move(n, x, y):
    if n < 1:
        return

    src = x
    dst = y
    tmp = 6 - src - dst

    if n == 1:
        print(1, src, dst)
    else:
        move(n - 1, src, tmp)
        print(n, src, dst)
        move(n - 1, tmp, dst)


N = int(input())
move(N, 1, 3)
