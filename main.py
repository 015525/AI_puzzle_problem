from tkinter import *
import tkinter as tk
from tkinter import messagebox
from Answer import mainAnswer
from BFS.BFS import BFS
from state.State import State
from astar.solver import solve
from DFS.DFS import DFS

#start page of the program
class App(tk.Tk):

    input = 0                                       # save user input
    algorithms = ['BFS', 'DFS', 'A*']               # available algorithm to use
    options = ["Manhattan","Euclidian"]             # available heuristic functions

    def __init__(self):                             # create main page
        super().__init__()
        self.x = IntVar()                           # hold number of the algorithm
        self.variable = StringVar(self)             # hold name of the heuristic function
        self.variable.set(self.options[0])          # initial value of the heuristic function is manhattan

        self.config(background='#FEEBA0')           # main page background color
        self.geometry("440x500")                    # size of the page
        self.resizable(False, False)                # set the page to fixed size
        self.title('8 Puzzle solver')               # page title

        self.frame = Frame(self)                    # set a frame to hold input components
        self.entry = Entry(self.frame,              # make entry field to read input from user
                           font=('Arial', 25))
        self.enter_button = Button(self.frame,      # make Enter button to enter the input
                                   text="Enter",
                                   command=self.check_input,
                                   font=("Arial", 20),
                                   bg = 'lightblue'
                                   )
        self.entry.pack(side=LEFT, expand=True)     # add the entry to the frame and fill the window
        self.enter_button.pack(side=RIGHT)          # put the button to the frame to the right of the entry
        self.frame.pack()                           # add the frame to the window

        for index in range(len(self.algorithms)):   # create radio button for each algorithm to choose from them
            if index != 2:
                self.radio_button = Radiobutton(self,
                                                text=self.algorithms[index],
                                                variable=self.x, # variable to hold the choose
                                                value=index,     # the value of each choose is its index
                                                padx=0,
                                                bg='#F5631A',
                                                width=10,
                                                indicatoron=0,
                                                font=('Arial', 25))
                self.radio_button.pack(anchor=W)  # add the radio buttons to window and set them to the west
            else:
                Aframe = Frame(self, bg = '#FEEBA0')
                self.radio_button = Radiobutton(Aframe,
                                                text=self.algorithms[index],
                                                variable=self.x,  # variable to hold the choose
                                                value=index,  # the value of each choose is its index
                                                padx=0,
                                                bg='#F5631A',
                                                width=10,
                                                indicatoron=0,
                                                font=('Arial', 25))

                self.radio_button.grid(row=0, column=0)
                menu = OptionMenu(Aframe, self.variable, *self.options)
                menu.config(state='normal', font=("Arial", 15), height=2)
                menu.grid(row=0, column=1)
                Aframe.pack(anchor=W)

        self.solve = Button(self,                   # add button to start solving the problem
                            text='Solve',
                            command=self.find_sol,
                            font=("Comic Sans", 20),
                            state=DISABLED         # disable the button until the user enter any input
                            )
        self.solve.pack(pady=20)                    # add the button to the window

    def check_input(self):
        initial = self.entry.get()                  # get the input from the user
        if '9' in initial or len(initial) != 9:     # check if the user entered valid input
            messagebox.showerror(title='error', message="incorrect input")
            self.solve.config(state=DISABLED)       # keep the button disabled as the input is not correct
        else:
            self.solve.config(state=ACTIVE)         # activate the input if the input is correct
            self.input = int(initial)               # turn the string input into integer

    def find_sol(self):
        found, explored, runtime, goal_path = False, [], 0, []
        depth, cost = 0, 0
        choose = self.x.get()                       # get the chosen algorithm from the user
        self.entry.delete(0, len(str(self.input)))  # remove the old input (we don't need it anymore)
        if choose == 0:                             # algorithm is BFS
            bfs = BFS(State(self.input))
            found, explored, runtime, goal_path, depth, cost = bfs.search()

        elif choose == 1:                           # algorithm is DFS
            dfs = DFS(State(self.input))
            found, explored, runtime, goal_path, depth, cost = dfs.run()

        elif choose == 2:                           # algorithm is A*
            found, explored, runtime, goal_path, depth, cost = solve(self.input, self.variable)
            runtime = round(runtime, 6)

        if not found:
            messagebox.showerror(title='error', message="this problem has no solution")
            self.solve.config(state=DISABLED)
        else:
            window = mainAnswer(goal_path, explored, depth, cost, runtime)
        self.solve.config(state=DISABLED)


if __name__ == '__main__':
    app = App()
    app.mainloop()
