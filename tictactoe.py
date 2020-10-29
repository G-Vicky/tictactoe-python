import tkinter as tk
import random
import tkinter.font as font
from tkinter import messagebox as mb


class TicTacToe(tk.Frame):
    def __init__(self):
        self.match_status = None

        tk.Frame.__init__(self)
        self.grid()
        self.master.title("TicTacToe")

        self.home_Page()
        
        self.mainloop()
    

    def home_Page(self):    #first page
        self.start_frame = tk.Frame(self, bd=3, width=300, height=300, bg="#233D46")
        self.start_frame.grid()

        self.player1_name = tk.StringVar(self.start_frame)
        self.player2_name = tk.StringVar(self.start_frame)
        
        player1_label = tk.Label(self.start_frame, text="Player 1", fg="white", bg="#233D46")
        player1_label.place(relx=0.2, rely=0.3, anchor="center")
        player1 = tk.Entry(self.start_frame, textvariable=self.player1_name)
        player1.place(relx=0.6, rely=0.3, anchor="center")
        
        player2_label = tk.Label(self.start_frame, text="Player 2", fg="white", bg="#233D46")
        player2_label.place(relx=0.2, rely=0.4, anchor="center")
        player2 = tk.Entry(self.start_frame, textvariable=self.player2_name)
        player2.place(relx=0.6, rely=0.4, anchor="center")
        
        start_btn = tk.Button(self.start_frame, text="Start game", command=self.start_Game)
        start_btn.place(relx=0.5, rely=0.6, anchor="center")


    def make_GUI(self):
        self.turn_player = self.player1            #game details
        self.turn_symbol = "X"
        self.match_status = None
        self.matrix = 3
        self.matrix_values = [[None]*3 for _ in range(3)]
        self.cells = []
        
        self.main_grid = tk.Frame(self, bd=3, width=600, height=600, bg="#233D46")
        self.main_grid.grid(pady=(100,0))
        
        label_font = font.Font(family="Helevetica", size=20)
        symbol_font = font.Font(family="courier", size=25, weight="bold")

        for i in range(self.matrix):           #initialize empty matrix
            row = []
            for j in range(self.matrix):
                cell_btn = tk.Button(self.main_grid, 
                    bg="gray", 
                    activebackground = "gray",
                    width=15, 
                    height=7,
                    fg="white",
                    activeforeground="white",
                    command=lambda m=i, n=j: self.clicked(m,n)
                )
                cell_btn.grid(row=i, column=j, padx=5, pady=5)
                cell_data = {"button": cell_btn}
                row.append(cell_data)
            self.cells.append(row)
        turn_frame = tk.Frame(self)         #game header!
        turn_frame.place(relx=0.5, y=45, anchor="center")
        # exit_btn = tk.Button(turn_frame, text="Exit", bg="red", command=self.exit_Game)
        # exit_btn.place(relx=0.5, rely=0.6, anchor="center")

        self.player_turn = tk.Label(turn_frame, text=self.turn_player+" 's turn", font=label_font)
        self.player_turn.grid(row=0)
        self.player_symbol = tk.Label(turn_frame, text=self.turn_symbol, font=symbol_font)
        self.player_symbol.grid(row=1)

    def clicked(self, row, col):
        if self.matrix_values[row][col] == None:
            self.cells[row][col]["button"].configure(
                text=self.turn_symbol,
                bg="#233D46", 
                activebackground="#233D46"
            )
            self.matrix_values[row][col] = self.turn_symbol
            self.checkMatrix(self.turn_symbol)
            if self.match_status == None:
                self.update_Turn(self.turn_player,self.turn_symbol)
            else:
                self.make_GUI()

    def update_Turn(self, player, symbol):
        if self.match_status == None:
                if symbol == "X":
                    self.turn_symbol = "O"
                    self.turn_player = self.player2
                    self.player_symbol.configure(text="O")
                    self.player_turn.configure(text=self.player2+" 's turn")
                else:
                    self.turn_symbol = "X"
                    self.turn_player = self.player1
                    self.player_symbol.configure(text="X")
                    self.player_turn.configure(text=self.player1+" 's turn")

        
    def checkMatrix(self,symbol):
        # for values in self.matrix_values:         todo implement draw logic
        #     if None not in values:
        #         self.main_grid.destroy()
        #         self.match_status = "won"
        #         mb.showinfo("Game results","Game draw")
        #         return

        self.count = 0
        for m in range(self.matrix):
            for n in range(self.matrix):
                if m == n and self.matrix_values[m][n] == symbol:
                        self.count += 1
        self.check()
        for m in range(self.matrix):
            for n in range(self.matrix):
                if (m+n == self.matrix - 1) and self.matrix_values[m][n] == symbol:
                        self.count += 1
        self.check()
        for m in range(self.matrix):
            for n in range(self.matrix):
                if self.matrix_values[m][n] == symbol:
                    self.count += 1
            self.check()
        for m in range(self.matrix):
            for n in range(self.matrix):
                if self.matrix_values[n][m] == symbol:
                    self.count += 1
            self.check()

    def check(self):
            if self.count == self.matrix:
                self.main_grid.destroy()
                self.count = 0
                self.match_status = "won"
                mb.showinfo("Game results", self.turn_player + " won the game")
            else:
                self.count = 0

    def start_Game(self):
        self.player1 = str(self.player1_name.get())
        self.player2 = str(self.player2_name.get())
        if self.player1 == "":
            mb.showerror("Invalid", "Enter player 1 name")
            return
        if self.player2 == "":
            mb.showerror("Invalid", "Enter player 2 name")
            return
        self.start_frame.destroy()
        self.make_GUI()

    def exit_Game(self):
        self.main_grid.destroy()
        self.home_Page()


TicTacToe()