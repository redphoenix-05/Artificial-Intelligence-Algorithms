board = [' ' for _ in range(9)]

def print_board(b):
    print()
    print(f" {b[0]} | {b[1]} | {b[2]} ")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]} ")
    print()

def winner(b, p):
    win = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(b[i] == b[j] == b[k] == p for i,j,k in win)

def draw(b):
    return ' ' not in b

def minimax(b, is_max):
    if winner(b, 'O'): return 1
    if winner(b, 'X'): return -1
    if draw(b): return 0

    if is_max:
        best = -100
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                best = max(best, minimax(b, False))
                b[i] = ' '
        return best
    else:
        best = 100
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                best = min(best, minimax(b, True))
                b[i] = ' '
        return best

def best_move(b):
    best_val = -100
    move = -1
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            move_val = minimax(b, False)
            b[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

print("Tic Tac Toe (You = X, AI = O)")
print("Positions:")
print("0 | 1 | 2")
print("3 | 4 | 5")
print("6 | 7 | 8")

while True:
    print_board(board)

    user = int(input("Enter your move (0-8): "))
    if board[user] != ' ':
        print("Invalid move!")
        continue

    board[user] = 'X'

    if winner(board, 'X'):
        print_board(board)
        print("🎉 You Win!")
        break

    if draw(board):
        print_board(board)
        print("🤝 Draw!")
        break

    ai = best_move(board)
    board[ai] = 'O'

    if winner(board, 'O'):
        print_board(board)
        print("🤖 AI Wins!")
        break
