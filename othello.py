NONE = ' '
BLACK = 'B'
WHITE = 'W'
class GameState:

    def __init__(self, col, row,turn, position):
        self._rows = row
        self._cols = col
        self._board = self.new_game_board()
        self._turn = turn
        self.set_piece(position.lower())
        self._blacks = 0
        self._whites = 0
        self._empty = (col * row)
        self.print_board()


        
    def new_game_board(self):
        board = []
        
        for row in range(self._rows):
            board.append([])
            for col in range(self._cols):
                board[-1].append(NONE)
                
        return board
    def print_board(self):
        counterblack=0
        counterwhite=0
        print('  ', end ='')
        for col in range(self._cols):
            if col < 10:
                print('0'+str(col), end = '  ')
            else:
                print(col, end = '  ')
        print()
        for row in range(self._rows):
            if row < 10:
                print('0'+str(row), end = ' ')
            else:
                print(row, end = ' ')
            for col in range(self._cols):
                if self._board[row][col] == NONE:
                    print('.', end = '   ')
                if self._board[row][col] == BLACK:
                    print('B', end = '   ')
                    counterblack += 1                    
                elif self._board[row][col] == WHITE:
                    print('W', end = '   ')
                    counterwhite += 1
            print()
        print('BLACK =' + str(counterblack) + '    WHITE =' + str(counterwhite))
        self._blacks = counterblack
        self._whites = counterwhite
        self._empty = self._rows * self._cols - (self._blacks + self._whites)
    def set_piece(self, white_or_black):
        '''used for setting the inputted piece at top left at the beginning of the game'''
        if white_or_black == 'white':
            self._board[int(self._rows/2)-1][int(self._cols/2)-1] = WHITE
            self._board[int(self._rows/2)-1][int((self._cols/2))] = BLACK
            self._board[int((self._rows/2))][int(self._cols/2)] = WHITE
            self._board[int((self._rows/2))][int(self._cols/2)-1] = BLACK
        if white_or_black == 'black':
            self._board[int(self._rows/2)-1][int(self._cols/2)-1] = BLACK
            self._board[int(self._rows/2)-1][int((self._cols/2))] = WHITE
            self._board[int((self._rows/2))][int(self._cols/2)] = BLACK
            self._board[int((self._rows/2))][int(self._cols/2)-1] = WHITE
              
    def is_valid(self, row, col, i, j):
        '''checks if move is valid, i and j representing left, right, up, down, or diagonal'''
        x = 0
        y = 0
        if self._turn == 'W':
            try:
                if self._board[row+(x+i)][col+(y+j)] == BLACK and self._board[row][col] == NONE and row+(x+i) != -1 and col+(y+j) != -1:
                        while self._board[row+(x+i)][col+(y+j)] == BLACK:
                            x += i
                            y += j
                            if self._board[row+(x+i)][col+(y+j)] == WHITE and row+(x+i) != -1 and col+(y+j) != -1:
                                return True
                            if self._board[row+(x+i)][col+(y+j)] == NONE:
                                return False
                else:
                    return False
            except:
                return False
        if self._turn == 'B':
            try:
                if self._board[row+(x+i)][col+(y+j)] == WHITE and self._board[row][col] == NONE and row+(x+i) >= 0 and col+(y+j) >= 0:
                    while self._board[row+(x+i)][col+(y+j)] == WHITE:
                        x += i
                        y += j
                        if self._board[row+(x+i)][col+(y+j)] == BLACK and (row+x+i) >= 0 and (col+y+j) >= 0:
                            return True
                        if self._board[row+(x+i)][col+(y+j)] == NONE:
                            return False
                else:
                    return False
            except:
                return False
    def flip_piece(self, row, col):
        '''flips piece'''
        counter = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.is_valid(row, col, i, j):
                    counter += 1
                    x = 0
                    y = 0
                    if self._turn == WHITE:
                        while self._board[row+(x+i)][col+(y+j)] == BLACK:
                            self._board[row+(x+i)][col+(y+j)] = WHITE
                            x += i
                            y += j
                    if self._turn == BLACK:
                        while self._board[row+(x+i)][col+(y+j)] == WHITE:
                            self._board[row+(x+i)][col+(y+j)] = BLACK
                            x += i
                            y += j
        if counter >= 1 and self._turn == WHITE:
            self._board[row][col] = WHITE
        if counter >= 1 and self._turn == BLACK:
            self._board[row][col] = BLACK
        if counter == 0:
            raise Exception
        self.turn_switch()
        self.print_board()
    def turn_switch(self):
        if self._turn == 'W':
            self._turn = 'B'
        else:
            self._turn ='W'
    def check_possible_moves(self):
        '''to check if the user with the turn has a possible move, otherwise changes turn'''
        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[row][col] == NONE:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if self.is_valid(row, col, i, j):
                                return True

def determine_winner(game: object, condition: str):
    winner = ''
    if condition == 'most':
        if game._blacks > game._whites:
            winner = 'Black'
        elif game._whites > game._blacks:
            winner = 'White'
        else:
            winner = 'Tie'
    if condition == 'fewest':
        if game._blacks < game._whites:
            winner = 'Black'
        elif game._whites < game._blacks:
            winner = 'White'
        else:
            winner = 'Tie'
    return winner
'''
x = GameState(4,4,'B', 'White')
x._board[0][0] = 'W'
x._board[0][1] = 'W'
x._board[0][2] = 'W'
x._board[0][3] = 'W'
x._board[1][0] = 'B'
x._board[1][1] = 'B'
x._board[1][2] = 'W'
x._board[2][0] = 'B'
x._board[2][1] = 'B'
x._board[2][2] = 'B'
x._board[2][3] = 'W'
x._board[3][0] = 'B'
x._board[3][1] = 'W'
x._board[3][2] = 'W'
x._board[3][2] = 'W'
'''



