startX = int(input())
startY = int(input())
endX = int(input())
endY = int(input())

diffX = startX - endX
diffY = startY - endY

if -1 <= diffX <= 1 and -1 <= diffY <= 1:
    print('YES')
else:
    print('NO')
