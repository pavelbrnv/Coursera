s = input()

i = 0
sLen = len(s)

while i < sLen - 1:
    print(s[i], end='')
    print('*', end='')
    i += 1

print(s[i])
