print("Welcome to tictactoe game :)")
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

winner = None
full = False
moves = []
game = True


def display():
    for i in board:
        print("-" * 7)
        for j in i:
            print("|" + j, end="")
        print("|")
    print("-" * 7)

display()


def win(player):
    global winner
    b = board
    hori = b[0][0] == b[0][1] == b[0][2] != ' ' or b[1][0] == b[1][1] == b[1][2] != ' ' or b[2][0] == b[2][1] == b[2][
        2] != ' '
    verti = b[0][0] == b[1][0] == b[2][0] != ' ' or b[0][1] == b[1][1] == b[2][1] != ' ' or b[0][2] == b[1][2] == b[2][
        2] != ' '
    dia = b[0][0] == b[1][1] == b[2][2] != ' ' or b[2][0] == b[1][1] == b[0][2] != ' '
    if hori or verti or dia:
        winner = player
    for i in board:
        if " " in i:
            full = False
            break
        else:
            full = True
    if full and not winner:
        winner = 'draw'


player = 'X'
while game:
    move = input(f"Player ({player}) coordinates: ")
    if move not in moves:
        moves.append(move)
    else:
        print("Already Occupied! ")
        continue
    try:
        y, x = int(move[0]), int(move[1])

        x -= 1
        if y == 1:
            y = 2
        elif y == 3:
            y = 0
        else:
            y -= 1
    except:
        print("Enter the Coordinates properly! ")
        continue
    board[2 - y][x] = f"{player}"

    display()
    win(player)
    if winner == player:
        print(f"{player} wins! ")
        game = False
    elif winner == "draw":
        print("It's a Tie")
        game = False
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
