def milestonegame():
    global board
    print('Welcome to tic tac toe game!')
    print('player X will go first')
    board = ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def printboard(board):
        print(board[7]+'|'+board[8]+'|'+board[9])
        print("_",'_','_')
        print(board[4]+'|'+board[5]+'|'+board[6])
        print("_",'_','_')
        print(board[1]+'|'+board[2]+'|'+board[3])
    printboard(board)
    def playerchoice():
        c = 1
        global board
        while ' ' in board:
            if c%2 ==0:
                choice = int(input('please choose the the location respective to your name pad'))
                while board[choice] != ' ':
                    print('invalid input, please try again')
                    choice = int(input('please choose the the location respective to your name pad'))
                board[choice]= 'O'
                c = c +1
                printboard(board)
                windec(board)
            else:
                choice = int(input('please choose the the location respective to your name pad'))
                while board[choice] != ' ':
                    print('invalid input, please try again')
                    choice = int(input('please choose the the location respective to your name pad'))
                board[choice]= 'X'
                printboard(board)
                c = c +1
                windec(board)
    def windec(board):
        if board[7]==board[8]==board[9]=='X':
            print('Player X is the winner')
        elif board[4]==board[5]==board[6]=='X':
            print('Player X is the winner')
        elif board[1]==board[2]==board[3]=='X':
            print('Player X is the winner')
        elif board[7]==board[4]==board[1]=='X':
            print('Player X is the winner')
        elif board[8]==board[5]==board[2]=='X':
            print('Player X is the winner')
        elif board[3]==board[6]==board[9]=='X':
            print('Player X is the winner')
        elif board[7]==board[5]==board[3]=='X':
            print('Player X is the winner')
        elif board[9]==board[5]==board[1]=='X':
            print('Player X is the winner')
        elif board[7]==board[8]==board[9]=='O':
            print('Player O is the winner')
        elif board[4]==board[5]==board[6]=='O':
            print('Player O is the winner')
        elif board[1]==board[2]==board[3]=='O':
            print('Player O is the winner')
        elif board[7]==board[4]==board[1]=='O':
            print('Player O is the winner')
        elif board[8]==board[5]==board[2]=='O':
            print('Player O is the winner')
        elif board[3]==board[6]==board[9]=='O':
            print('Player O is the winner')
        elif board[7]==board[5]==board[3]=='O':
            print('Player O is the winner')
        elif board[9]==board[5]==board[1]=='O':
            print('Player O is the winner')
        elif ' ' not in board:
            print("ITS A DRAW!!")
        else:
            pass
    playerchoice()
    windec(board)
    choicey = 'wrong'
    choicey = input('would you like to play again?, reply with \'Y\' OR \'N\'')
    while choicey not in ["y",'n','Y','N']:
        print("Sorry, thats not \'Y\' OR \'N\', please reply with \'Y\' OR \'N\'")
        choicey = input('would you like to play again?, reply with \'Y\' OR \'N\'')
    if choicey == "Y" or 'y':
        milestonegame()
    elif choicey == 'N' or 'n':
        print("Thanks for playing!")
    else:
        pass


milestonegame()
        
        
            
        
        

        
