import tkinter as tk
import random
import tkinter.font as font
from tkinter import messagebox as mb


class TicTacToe(tk.Frame):
    def __init__(self):
        self.turn_symbol = "X"
        self.player1_name = "player1"
        self.player2_name = "player2"
        self.matrix_values = [[None]*3 for _ in range(3)]

        tk.Frame.__init__(self)
        self.grid()
        self.master.title("TicTacToe")

        self.main_grid = tk.Frame(self, bd=3, width=600, height=600, bg="#233D46")
        self.main_grid.grid(pady=(100,0))
        self.make_GUI()
        
        self.mainloop()
    
    def make_GUI(self):
        self.cells = []
        self.matrix = 3
        label_font = font.Font(family="Helevetica", size=20)
        symbol_font = font.Font(family="courier", size=15, weight="bold")
        for i in range(self.matrix):
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

        #header plyer's turn
        turn_frame = tk.Frame(self)
        turn_frame.place(relx=0.5, y=45, anchor="center")
        self.player_turn = tk.Label(turn_frame, text=self.player1_name+" 's turn", font=label_font)
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
            if self.turn_symbol == "X":
                self.turn_symbol = "O"
                self.player_symbol.configure(text="O")
                self.player_turn.configure(text=self.player2_name+" 's turn")
            else:
                self.turn_symbol = "X"
                self.player_symbol.configure(text="X")
                self.player_turn.configure(text=self.player1_name+" 's turn")
        
    def checkMatrix(self,symbol):
        count = 0
        for m in range(self.matrix):
            for n in range(self.matrix):
                if m == n:
                    if self.matrix_values[m][n] == symbol:
                        print("checking")
                        count += 1
        if count == 3:
            print("won")
            mb.showinfo("Game results", "player 1 won the game")
TicTacToe()