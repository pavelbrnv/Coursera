n = int(input())

if n > 1:
    far = 0
    near = 1
    index = 2

    while index < n:
        new = far + near
        far = near
        near = new
        index += 1

    print(far + near)

elif n == 1:
    print(1)
else:
    print(0)
