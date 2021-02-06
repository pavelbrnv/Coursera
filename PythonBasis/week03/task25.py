s = input()

i = 0
sLen = len(s)

while i < sLen:
    if i % 3 != 0:
        print(s[i], end='')
    i += 1
