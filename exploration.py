from tkinter import *
import tkinter as tk

from AI_puzzle_problem.state.State import State

from AI_puzzle_problem.BFS.BFS import BFS


class Explore(tk.Toplevel):
    count = 0

    def __init__(self, expanded):
        super().__init__()
        self.list = expanded
        self.config(bg='orange')
        # root window
        self.geometry("400x500")
        self.title('path to goal')
        self.resizable(1, 1)
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_widgets()

    def create_widgets(self):
        num = self.list[self.count]
        display = str(num)
        if len(display) == 8:
            display = "0" + display

        index = 0
        for i in range(3):
            for j in range(3):
                t = ""
                if display[index] != '0':
                    t = display[index]
                cell = Label(self, text=t, font=("Arial", 15), height=3, width=20)
                cell.grid(column=j, row=i, padx=3, pady=3)
                index += 1

        next_button = Button(self, text="Next", font=("Arial", 15), command=self.next_state)
        next_button.grid(column=2, row=3, padx=5, pady=20)

        ex = Button(self, text="exit this page", font=("Arial", 15), command=self.return_to_main)
        ex.grid(column=1, row=3, padx=5, pady=20)

        previous = Button(self, text="previous",font=("Arial", 15), command=self.previous_state)
        previous.grid(column=0, row=3, padx=5, pady=20)

        path = Label(self, text="path: " +str(self.count+1) + "\\" +str(len(self.list)), font=("Arial", 15))
        path.grid(column=0, row=5, padx=3, pady=10, columnspan=1)

        if self.count >= (len(self.list)-1):
            next_button["state"] = "disabled"

        if self.count <= 0:
            previous["state"] = "disabled"

    def next_state(self):
        self.count += 1
        self.create_widgets()

    def previous_state(self):
        self.count -= 1
        self.create_widgets()

    def return_to_main(self):
        self.destroy()


if __name__ == "__main__":
    bfs = BFS(State(125340678))
    found, explored,run_time, path = bfs.search()
    app = Explore(explored)

    app.mainloop()
