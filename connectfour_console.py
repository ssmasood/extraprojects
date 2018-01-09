import connectfour
def pop_n_drop(GAME: object, user_input, column_number):
    try:
        if user_input == "DROP":
            GAME = connectfour.drop_piece(GAME, (int(column_number)-1))
        if user_input == "POP":
            GAME = connectfour.pop_piece(GAME, (int(column_number)-1))
        print_board(GAME)
    except:
        print("Column number must be from 1-7")
    return GAME
def print_board(game_state: object):

    for i in range(connectfour.BOARD_ROWS):
        for j in range(connectfour.BOARD_COLUMNS):
            if game_state.board[j][i] == connectfour.NONE:
                print('.', end = '   ')
            elif game_state.board[j][i] == connectfour.RED:
                print('R', end = '   ')
            elif game_state.board[j][i] == connectfour.YELLOW:
                print('Y', end = '   ')
        print()
def determine_winner(GAME: object):
    if connectfour.winning_player(GAME) != ' ':
        print("We have a winner " + connectfour.winning_player(GAME) + "!!!!")
        return False
def valid(game_state, drop_pop):   
    assert drop_pop.upper() == 'DROP' or drop_pop.upper()== 'POP'
    
def drop_input():
    drop_pop = input("Please enter Drop or Pop: ")
    return drop_pop.upper()

