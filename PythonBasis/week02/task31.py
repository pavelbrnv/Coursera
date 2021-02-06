current = int(input())
m = current

while current != 0:
    current = int(input())
    if current != 0 and current > m:
        m = current

print(m)
