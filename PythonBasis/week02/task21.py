a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0:
    if b != 0:
        print('NO')
    else:
        if c == 0 and d == 0:
            print('NO')
        else:
            print('INF')
elif -b % a != 0 or (c == 0 and d == 0):
    print('NO')
else:
    x = -b // a
    if c == 0:
        print(x)
    else:
        if -d % c == 0 and x == -d // c:
            print('NO')
        else:
            print(x)
