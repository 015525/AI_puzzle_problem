from tkinter import *
import tkinter as tk
from tkinter import messagebox


class noSol(tk.Tk):

    def __init__(self, run_time, explored_len):
        super().__init__()
        self.config(background='orange')
        self.geometry("440x500")
        self.resizable(False, False)
        self.title('8 Puzzle solver')

        back_button = Button(self, text="back", font=("Arial", 15))
        back_button.pack(anchor='w')

        label = Label(self, text="this problem has no solution", font=("Arial", 25), bg='red')
        label.pack(expand=True)


if __name__ == '__main__':
    no_sol = noSol(0, 0)
    no_sol.mainloop()
