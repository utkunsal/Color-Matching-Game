import sys
with open(sys.argv[1]) as f:
    board = [x.strip().split() for x in f.readlines()]

def view():
    for x in board:
        print(*x)
    print()

score = 0
def upd_score(x, y):
    # x and y are coordinates.
    global score
    ball = board[y][x]
    if ball == "B": score += 9
    elif ball == "G": score += 8
    elif ball == "W": score += 7
    elif ball == "Y": score += 6
    elif ball == "R": score += 5
    elif ball == "P": score += 4
    elif ball == "O": score += 3
    elif ball == "D": score += 2
    elif ball == "F": score += 1

def disappear(x, y):
    # x and y are coordinates.
    color = board[y][x]
    if color == "X":
        board[y][x] = " "
        for y1 in range(len(board)):
            upd_score(x, y1)
            if board[y1][x] == "X":
                disappear(x, y1)
            board[y1][x] = " "
        for x1 in range(len(board[0])):
            upd_score(x1, y)
            if board[y][x1] == "X":
                disappear(x1, y)
            board[y][x1] = " "
    else:
        upd_score(x, y)
        board[y][x] = " "
        if x+1 < len(board[0]):
            if board[y][x + 1] == color:
                disappear(x + 1, y)
        if x-1 >= 0:
            if board[y][x - 1] == color:
                disappear(x - 1, y)
        if y+1 < len(board):
            if board[y + 1][x] == color:
                disappear(x, y + 1)
        if y-1 >= 0:
            if board[y - 1][x] == color:
                disappear(x, y - 1)

def move_down():
    for repeat in range(len(board)-1):
        for y in range(1, len(board)):
            for x in range(len(board[0])):
                if board[y][x] == " ":
                    board[y][x] = board[y-1][x]
                    board[y-1][x] = " "
    for x in range(len(board)-1):
        if board[0].count(" ") == len(board[0]):
            board.pop(0)

def move_left():
    x = 0
    while x < len(board[0]):
        if board[-1][x] == " ":
            for row in board:
                row.pop(x)
        else:
            x += 1

def game_not_over():
    if board == []:
        return False
    else:
        for x in range(len(board[0])):
            for y in range(len(board)):
                if x+1 < len(board[0]):
                    if board[y][x] == board[y][x+1] and board[y][x] != " ":
                        return True
                if y+1 < len(board):
                    if board[y][x] == board[y+1][x] and board[y][x] != " ":
                        return True
                if board[y][x] == "X":
                    return True

def has_neighbor(x, y):
    # x and y are coordinates.
    if x + 1 < len(board[0]):
        if board[y][x] == board[y][x + 1]: return True
    if y + 1 < len(board):
        if board[y][x] == board[y + 1][x]: return True
    if x - 1 >= 0:
        if board[y][x] == board[y][x - 1]: return True
    if y - 1 >= 0:
        if board[y][x] == board[y - 1][x]: return True

print()
view()
print(f"Your score is: {score}\n")
while game_not_over():
    inp = input("Please enter a row and column number: ").split()
    print()
    try:
        row, colm = int(inp[0]), int(inp[1])
        if row < 0 or row >= len(board) or colm < 0 or colm >= len(board[0]) or board[row][colm] == " ":
            print("Please enter a valid size!\n")
        else:
            if board[row][colm] == "X" or has_neighbor(colm, row):
                disappear(colm, row)
                move_down()
                if board != []: move_left()
            if board != [[]]: view()
            print(f"Your score is: {score}\n")
    except Exception:
        print("Please enter a valid size!\n")
print("Game over!\n")
