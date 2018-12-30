from random import randint

board = {1:' ', 2:' ', 3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' '}

def drawBoard():
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('---+---+---')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('---+---+---')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])

def isWinner():
    return any([board[1]==turn and board[2]==turn and board[3]==turn,        #1st row
                board[4]==turn and board[5]==turn and board[6]==turn,        #2nd row
                board[7]==turn and board[8]==turn and board[9]==turn,        #3rd row
                board[1]==turn and board[4]==turn and board[7]==turn,        #1st column
                board[2]==turn and board[5]==turn and board[8]==turn,        #2nd column
                board[3]==turn and board[6]==turn and board[9]==turn,        #3rd column
                board[1]==turn and board[5]==turn and board[9]==turn,        #1st diagonal
                board[3]==turn and board[5]==turn and board[7]==turn])       #2nd diagonal

def playerMove():
    move = 0
    while move not in possibleMoves:
        move = int(input("Your turn.\nMove on which space? ("+",".join([str(x) for x in possibleMoves])+") : "))
    possibleMoves.remove(move)
    board[move] = player

def computerMove():
    print("Computer's turn...")
    poss = 0
    for x in possibleMoves:
        board[x] = player
        if isWinner():
            poss = x
            board[x] = ' '
            break
        board[x] = ' '
    if poss: move = poss
    else: move = possibleMoves[randint(0,len(possibleMoves)-1)]
    possibleMoves.remove(move)
    board[move] = computer

print('Hello player! Welcome to the TIC-TAC-TOE game!')
player = ''
while player == '' and player != 'X' and player != 'O': player = input("Do you want to be 'X' or 'O' : ").upper()

if player == 'X': computer = 'O'
else: computer = 'X'

turn, possibleMoves = ['O','X'][randint(0,1)], [i for i in range(1,10)]
if turn == player: print("You go first.")
else: print("Computer will go first.")

while True:
    if len(possibleMoves) == 0: break
    if turn == player: playerMove()
    else: computerMove()
    drawBoard()
    if isWinner(): break
    if turn == player: turn = computer
    else: turn = player

if isWinner() and turn == player: print("Hurrayy! You've beaten the computer. You won.")
elif isWinner() and turn == computer: print("Oops! The computer has beaten you. You lose.")
else: print("Oops! This is a draw. Nobody won the game.")
