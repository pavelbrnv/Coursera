a = int(input())

if a > 1:
    near = 1
    current = 1
    index = 2

    while current < a:
        new = near + current
        near = current
        current = new
        index += 1

    if current == a:
        print(index)
    else:
        print(-1)

elif a == 1:
    print(1)
else:
    print(0)
