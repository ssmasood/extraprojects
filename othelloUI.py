import othello
import othellocommands
def user_commands():
        rows = othellocommands.get_row()
        cols = othellocommands.get_col()
        turn = othellocommands.get_turn()
        position = othellocommands.get_position()
        condition = othellocommands.get_condition()
        othellocommands.start_game(cols, rows, turn, position, condition)
        


if __name__ == '__main__':
    user_commands()
