# First we're going to make the tic-tac-toe board
def draw_board(board):
    print("---------")
    for i in range(3):
        print("|", board[i][0], board[i][1], board[i][2], "|")
        # In board[a][b], [a] is the row, [b] is the column. Since i = " ", our board looks empty.
    print("---------")

board = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
x = 1  # x will be our player and it will alternate between player 1 and player 2
c = 9  # c is the amount of spaces we have in the board, we'll use it in order to see if the game is draw or not

#Then we're going to get user input
def play(x, c):
    while True:
        draw_board(board)
        try: 
            # Both row and column need to be extracted by 1 because of our list in board, which makes the rows/columns start from 0 and end in 2.         
            row = int(input(f"Player {x} select a row: ")) - 1
            column = int(input(f"Player {x} select a column: ")) - 1
       
            if row > 2 or row < 0 or column > 2 or column < 0:
                print("Please enter valid row/column.")
                return play(x, c)
            
            if board[row][column] != " ":
                return play(x, c)
            
            if x == 1:
                x = x + 1
                board[row][column] = "X"

            else:
                x = x - 1
                board[row][column] = "O"
            
            # We want to see how the game ends.
            # Horizontal win
            if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " " or board[1][0] == board[1][1] == board[1][2] and board[1][0] != " " or board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ":
                if x == 1:
                    x = x + 1
                elif x != 1:
                    x = x - 1
                draw_board(board)
                print(f"Player {x} has won the game !")
                break
                
            # Vertical win
            elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != " " or board[0][1] == board[1][1] == board[2][1] and board[0][1] != " " or board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
                if x == 1:
                    x = x + 1
                elif x != 1:
                    x = x - 1
                draw_board(board)
                print(f"Player {x} has won the game !")
                break
                
            # Diagonal win
            elif board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] and board[1][1] != " ":
                if x == 1:
                    x = x + 1
                elif x != 1:
                    x = x - 1
                draw_board(board)
                print(f"Player {x} has won the game !")
                break
                   
            # Draw 
            c = c - 1
            if c == 0:
                draw_board(board)
                print("It's a draw !")
                break                                         

        except ValueError:         
                print("Please enter integers only.")            


play(x, c)