from tkinter import *
import tkinter as tk
from tkinter import messagebox

from AI_puzzle_problem.BFS.BFS import BFS
from AI_puzzle_problem.state.State import State


class App(tk.Tk):
    input = 0
    algorithms = ['BFS', 'BFS', 'A*']

    def __init__(self):
        super().__init__()
        self.x = IntVar()
        self.config(background='orange')
        self.geometry("440x500")
        self.resizable(False, False)
        self.title('8 Pazzle solver')
        self.frame = Frame(self)
        self.entry = Entry(self.frame, font=('Arial', 25))
        self.enter_button = Button(self.frame,
                                   text="Enter",
                                   command=self.check_input,
                                   font=("Comic Sans", 20)
                                   )
        self.entry.pack(side=LEFT, expand=True)
        self.enter_button.pack(side=RIGHT)
        self.frame.pack()
        for index in range(len(self.algorithms)):
            self.radio_button = Radiobutton(self,
                                            text=self.algorithms[index],
                                            variable=self.x,
                                            value=index,
                                            padx=25,
                                            bg='red',
                                            indicatoron=0,
                                            font=('Impact', 25))

            self.radio_button.pack(anchor=W)

        self.solve = Button(self,
                            text='Solve',
                            command=self.find_sol,
                            font=("Comic Sans", 20),
                            state=DISABLED
                            )
        self.solve.pack()

    def check_input(self):
        initial = self.entry.get()
        if '9' in initial or len(initial) != 9:
            messagebox.showerror(title='error', message="incorrect input")
            self.solve.config(state=DISABLED)
        else:
            self.solve.config(state=ACTIVE)
            self.input = int(initial)

    def find_sol(self):
        found, expanded, frontier, parents, runtime = False, [], [], {}, 0
        depth, cost, path = 0, 0, []
        choose = self.x.get()
        if choose == 0:
            bfs = BFS(State(self.input))
            found, expanded, frontier, parents, runtime = bfs.search()
            depth = bfs.get_depth()
            cost = bfs.get_cost()
            path = bfs.goal_path





if __name__ == '__main__':
    app = App()
    app.mainloop()