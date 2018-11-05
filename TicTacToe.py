theBoard={'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
          'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
          'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('-+-+-')

def checkBoard(board):
    if board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X':
        return 'X'
    if board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X':
        return 'X'
    if board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X':
        return 'X'
    
    if board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O':
        return 'O'
    if board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O':
        return 'O'
    if board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O':
        return 'O'

    if board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X':
        return 'X'
    if board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X':
        return 'X'
    if board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X':
        return 'X'
    
    if board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O':
        return 'O'
    if board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O':
        return 'O'
    if board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O':
        return 'O'

    if board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X':
        return 'X'
    if board['low-L'] == 'X' and board['mid-M'] == 'X' and board['top-R'] == 'X':
        return 'X'

    if board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O':
        return 'O'
    if board['low-L'] == 'O' and board['mid-M'] == 'O' and board['top-R'] == 'O': 
        return 'O'  
    else:
        return 'N' 


printBoard(theBoard)

turn = 'X'
for i in range(9):
    print('Move: top-L, top-M, top-R\n mid-L, mid-M, mid-R\n low-L, low-M, low-R')
    print('Turn for '+ turn + ':')
    move = raw_input()
    theBoard[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
    printBoard(theBoard)
    result = checkBoard(theBoard)
    
    if result == 'X':
        print('X WIN')
        break
    if result == 'O':
        print('O WIN')
        break
   