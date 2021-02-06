n = int(input())

if n >= 1:
    val = 1
    print(val, end=' ')

    while val * 2 <= n:
        val = val * 2
        print(val, end=' ')
