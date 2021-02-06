a = int(input())
b = int(input())
c = int(input())

base = a
side1 = b
side2 = c

if b > base:
    base = b
    side1 = a
    side2 = c

if c > base:
    base = c
    side1 = a
    side2 = b

baseSqr = base**2
sidesSqr = side1**2 + side2**2

if base <= 0 or side1 <= 0 or side2 <= 0 or base >= side1 + side2:
    print('impossible')
elif baseSqr == sidesSqr:
    print('rectangular')
elif baseSqr < sidesSqr:
    print('acute')
elif baseSqr > sidesSqr:
    print('obtuse')
