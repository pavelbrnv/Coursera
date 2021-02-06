n = int(input())

i = 2
rem = n % i

while rem != 0:
    i += 1
    rem = n % i

print(i)
