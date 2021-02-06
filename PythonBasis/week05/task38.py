n, k = map(int, input().split())

states = [1] * n
for i in range(k):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        states[j - 1] = 0

for state in states:
    if state > 0:
        print('I', end='')
    else:
        print('.', end='')
