import othello
def get_row():
        while True:
            try:
                rows = int(input('ROWS: Please enter an even integer between 4 and 16(inclusive)'))    
                if (rows%2) == 0:
                        return rows
                else:
                        print('Not an even integer between 4 and 16(inclusive)')
            except:
                print('Not an integer')
def get_col():
        while True:
            try:
                cols = int(input('COLUMNS: Please enter an even integer between 4 and 16(inclusive)'))
                print()
                if (cols%2) == 0:
                        return cols
                else:
                        print('Not an even integer between 4 and 16(inclusive)')
            except:
                print('Not an integer')
def get_turn():
        while True:
                turn = input('Who goes first? Type "W" or "B"').upper()
                print()
                if (turn) == 'W' or turn == 'B':
                        return turn
                else:
                        print('Please type "W" or "B"')
def get_position():
        while True:
                position = input('Please enter which piece should go on the top left and bottom right[Type "white" or "black"]').lower()
                print()
                if position == 'white' or position == 'black':
                        return position
                else:
                        print('Please type "white" or "black"')

def get_condition():
        while True:
                condition = input('Win condition: Most or Fewest discs? [most/fewest]').lower()
                print()
                if condition == 'most' or condition == 'fewest':
                        return condition
                else:
                        print('Please type "most" or "fewest"')
def start_game(cols, rows, turn, position, condition):
        game = othello.GameState(cols, rows, turn, position)
        while True:
            print('It is '+ game._turn + "'s turn")
            print()
            if game.check_possible_moves():
                try:
                    row = int(input('ROW: Please enter the row where you want to put a piece on'))
                    col = int(input('COLUMN: Please enter the column where you want to put a piece on'))
                    game.flip_piece(row, col)
                except:
                    print('Invalid row/column, try again')
                finally:
                    counter = 0
            else:
                print('No possible moves for ' + game._turn)
                counter += 1
                if counter >= 2:
                    break
                game.turn_switch()
        print()
        print()
        print()
        print ("THE WINNER IS: " + othello.determine_winner(game, condition))

