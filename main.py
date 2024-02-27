from notakto import draw_board, has_line, place_x
def main():
    turn = 0
    board = [[''] * 3 for _ in range(3)]

    while True:
        draw_board(board)
        user_input = int(input(f"Player {turn % 2 + 1}'s turn (Enter a location to place X): "))
        if place_x(board, user_input):
            turn += 1
            if has_line(board):
                break
        else:
            print("Location invalid or already taken. Please try again.")
    draw_board(board)
    print(f"Player {turn % 2 + 1} wins!")
main()
    # initilalize turn to keep track of players 1 turn or players 2 turn
    # intitialize a 3X3 board and set as empty {}
    # initialize an index to kep track of user input

    # loop using while true
        # call function to draw board
        # print out whose turn using mod 2 and prompt them to enter location
        # take user input
    
        # if place x is on board is true then increment the turn
            # check if there is a line, if there is then break and game ends, else do nothing
        # else location is already taken so try again
    

    # draw final board 
    # state winer of game

