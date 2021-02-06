a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# sorting
if b < a:
    (a, b) = (b, a)
if c < b:
    (b, c) = (c, b)
if b < a:
    (a, b) = (b, a)

brickSmall = a
brickLarge = b

if e < d:
    (d, e) = (e, d)

holeSmall = d
holeLarge = e

if brickSmall <= holeSmall and brickLarge <= holeLarge:
    print('YES')
else:
    print('NO')
