import connectfour
import connectfour_console
def playgame(GAME: object):
    game_is_playing = True
    while game_is_playing == True:
        try:
            print("It is " + GAME.turn + "'s turn")
            user_input = connectfour_console.drop_input()
            column_number = int(input('Please enter a column number from 1 to 7'))
            connectfour_console.valid(GAME, user_input)
            GAME = connectfour_console.pop_n_drop(GAME, user_input, column_number)
            if connectfour_console.determine_winner(GAME) == False:
                game_is_playing = False
        except:
            print("Invalid user input")
if __name__ == '__main__':
    GAME = connectfour.new_game_state()
    playgame(GAME)
    
