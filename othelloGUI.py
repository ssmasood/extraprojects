import othellocommands
import othello
import tkinter
_BACKGROUND_COLOR = '#1A640F'

class InputApp:
    def __init__(self):
        self._root_window = tkinter.Tk()
        
        tkinter.Label(self._root_window, text= 'Rows(4 to 16 even digits)').grid(row=0)
        tkinter.Label(self._root_window, text= 'Cols(4 to 16 even digits)').grid(row=1)
        tkinter.Label(self._root_window, text= 'Turn(W or B)').grid(row=2)
        tkinter.Label(self._root_window, text= 'Top left piece(White or Black)').grid(row=3)
        tkinter.Label(self._root_window, text= 'Win Condition:(Most or Fewest)').grid(row=4)
        
        tkinter.Button(self._root_window, text= 'New Game', command = self.thegame).grid(row=5,column=0)
        tkinter.Button(self._root_window, text= 'Quit', command = self._root_window.destroy).grid(row=5,column = 1)
        
        self._e1 = tkinter.Entry(self._root_window)
        self._e2 = tkinter.Entry(self._root_window)
        self._e3 = tkinter.Entry(self._root_window)
        self._e4 = tkinter.Entry(self._root_window)
        self._e5 = tkinter.Entry(self._root_window)

        self._e1.grid(row=0, column =1)
        self._e2.grid(row=1, column =1)
        self._e3.grid(row=2, column =1)
        self._e4.grid(row=3, column =1)
        self._e5.grid(row=4, column =1)
        
    def thegame(self):
        x = [self._e1.get(),self._e2.get(),self._e3.get(),self._e4.get(),self._e5.get()]
        try:
            if (int(x[0]) <= 16 and int(x[0]) >= 4 and int(x[1]) <= 16 and int(x[1]) >= 4 and (x[2].upper() == 'W' or x[2].upper() == 'B') and (x[3].lower() == 'white' or x[3].lower() == 'black') and (x[4].lower() == 'most' or x[4].lower() == 'fewest')):
                
                OthelloApplication(othello.GameState(int(x[0]),int(x[1]), str(x[2]).upper(), str(x[3]).lower()), x[4]).start()
        except:
            pass
class OthelloApplication:
    def __init__(self, state: othello.GameState, condition: str):
        self._state = state
        self._condition = condition
        self._root_window = tkinter.Tk()
        
        self._canvas = tkinter.Canvas( master = self._root_window,
                                       width = 600, height = 600,
                                       background = _BACKGROUND_COLOR)
        self._canvas.grid(row = 1, column = 0, padx = 30, pady = 30,
                          sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        
        self._button = tkinter.Button(master =self._root_window, text = 'Quit', font = ('Helvetica', '15'),command = self._root_window.destroy)
        self._button.grid(row = 3, column = 0, padx = 10, pady = 10, stick = tkinter.S + tkinter.E)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        
        self._root_window.update()
        
        self._state.print_board()
        
        self.draw_lines()
        self._counter = 0

    def start(self) -> None:
        self._root_window.mainloop()

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self.draw_lines()

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        
        xsteps = int(width/self._state._cols)
        ysteps = int(height/self._state._rows)
        
        if self._state.check_possible_moves():
            for i in range(self._state._rows):
                for j in range(self._state._cols):
                    if event.y >= ysteps * i and event.y <= ysteps * (i+1) and event.x >= xsteps * j and event.x <= xsteps * (j+1):
                        try:
                            self._state.flip_piece(i, j)
                        except:
                            None
        self.draw_lines()
        if self._state.check_possible_moves() != True:
            self._state.turn_switch()
            if self._state.check_possible_moves() != True:
                popup_msg('The winner is: ' + othello.determine_winner(self._state, self._condition))
            
                
    
    def draw_lines(self) -> None:
        self._canvas.delete(tkinter.ALL)
        
        button1 = tkinter.Button(master = self._root_window, text = 'Black: '+ str(self._state._blacks), font = ('Helvetica', 20))
        button1.grid( row = 0, column =0, padx = 10, pady = 10, sticky = tkinter.W)
        
        button2 = tkinter.Button(master = self._root_window, text = 'White: ' + str(self._state._whites), font = ('Helvetica', 20))
        button2.grid ( row = 0, column = 2, padx = 10, pady=10, sticky = tkinter.E + tkinter.S)
        
        button3 = tkinter.Button(master = self._root_window, text = 'Turn:' + self._state._turn, font = ('Helvetica', 20))
        button3.grid(row = 0, column = 1, padx = 10, pady=10)
        
        self._root_window.update()
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        
        xsteps = int(width/self._state._cols)
        ysteps = int(height/self._state._rows)

        for i in range(xsteps, width, xsteps):
            self._canvas.create_line(i, 0, i, height, fill = 'black')
        for i in range(ysteps, height, ysteps):
            self._canvas.create_line(0, i, width, i, fill = 'black')
        for i in range(self._state._rows):
            for j in range(self._state._cols):
                x = xsteps * i
                y = ysteps * j
                if self._state._board[j][i] == 'B':
                    self._canvas.create_oval(x, y, x+xsteps, y+ysteps, fill = 'black')
                if self._state._board[j][i] == 'W':
                    self._canvas.create_oval(x, y, x+xsteps, y+ysteps, fill = 'white')
def popup_msg(msg):
    popup = tkinter.Tk()
    popup.wm_title("Game Over")
    label = tkinter.Label(popup, text=msg, font='Helvetica, 15')
    label.pack(side="top", fill="x", pady=10)
    button = tkinter.Button(popup, text="Quit", command = popup.destroy)
    button.pack()
    popup.mainloop()
                  

if __name__ == '__main__':
    x = InputApp().thegame()
    
