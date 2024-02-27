    # initialize and index to number the board
    # for loop stops at 3 
            # print straight line 
            # for loop stops at 3 
                # print top portion boxes
                # increment index for number board
            # close the box

            # for loop to handle placement of x
                # if board[i][j] is true then place x if false place " '"
            # close the box
    # print straight line
def draw_board(board):
    index = 1
    for i in range(3):
        # i = row
        print("-------------")
        for j in range(3):
            print(f"| {index} ", end= '' )
            index+=1
        print("|")

        for j in range(3):
            # j = column 
            print("| "+ ("X" if board[i][j] else " ")+ " ", end="")
        print("|")
    print("-------------")


    # for loop 
        # Check horizontally
        # or
        # check vertically
            # return true if checks are true

    # check for diagnoal cases return true if so 

    # if none return true then return false
def has_line(board):
    for i in range(3):
        if (board[i][0] and board[i][1] and board[i][2] or 
            board[0][i] and board[1][i] and board[2][i]):
            return True
        
        return (board[0][0] and board[1][1] and board[2][2] or 
                board[0][2] and board[1][1] and board[2][0])


    # check if idx between 1 - 9
    # if not then return false

    # given number between indices 1-9
    # conver number to array indices i and j
    # i = (number - 1) / 3
    # j = (number - 1) % 3

    # if the board already contains X (true) return false
    # otherwise modify the board to have an X (true) at the index, then return true
def place_x(board, idx):
    if idx < 1 or idx > 9:
        return False
    
    i = int((idx - 1) / 3)
    j = int((idx - 1) % 3)

    # if there already is an X (true), return false
    if board[i][j]:
        return False
    
    # otherwise, modify the board to have an X (true) at the index, then return true
    board[i][j] = True
    return True