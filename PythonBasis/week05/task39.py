BoardSize = 8


def CheckQueenAttack(board, x, y):
    # lines
    for i in range(BoardSize):
        # horizontal
        if i != x and board[i][y] == 1:
            return True

        # vertical
        if i != y and board[x][i] == 1:
            return True

    # diagonals
    for i in range(1, BoardSize):
        leftX = x - i
        if leftX >= 0:
            if y - i >= 0 and board[leftX][y - i] == 1:
                return True
            if y + i < BoardSize and board[leftX][y + i] == 1:
                return True

        rightX = x + i
        if rightX < BoardSize:
            if y - i >= 0 and board[rightX][y - i] == 1:
                return True
            if y + i < BoardSize and board[rightX][y + i] == 1:
                return True

    return False


def CheckQueensCrossing(positions):
    board = [[0 for x in range(BoardSize)] for y in range(BoardSize)]

    for position in positions:
        board[position[0]][position[1]] = 1

    for position in positions:
        if CheckQueenAttack(board, position[0], position[1]):
            return True

    return False


queensPositions = []
for tmp in range(0, 8):
    queenX, queenY = map(int, input().split())
    queensPositions.append([queenX - 1, queenY - 1])

if CheckQueensCrossing(queensPositions):
    print('YES')
else:
    print('NO')
