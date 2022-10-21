from tkinter import *
import tkinter as tk

from AI_puzzle_problem.state.State import State

from AI_puzzle_problem.BFS.BFS import BFS


class App(tk.Tk):
    count = 0

    def __init__(self, path_list, expanded2, depth2, time2):
        super().__init__()
        self.list = path_list
        self.path = path_list
        self.expanded_list = expanded2
        self.time = time2
        self.depth = depth2
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

        self.count += 1
        index = 0
        for i in range(3):
            for j in range(3):
                cell = Label(self, text=display[index], font=("Arial", 15), height=3, width=20)
                cell.grid(column=j, row=i, padx=10, pady=10)
                index += 1

        next_button = Button(self, text="Next", command=self.create_widgets)
        next_button.grid(column=2, row=3, sticky=tk.E, padx=5, pady=20)

        expanded_button = Button(self, text="Expanded",
                                     command=lambda: [f() for f in [self.show_expanded, self.create_widgets]])
        expanded_button.grid(column=0, row=3, sticky=tk.E, padx=5, pady=20)

        depthLabel = Label(self, text="Depth:   " + str(self.depth))
        depthLabel.grid(column=0, row=4, sticky=tk.E, padx=5, pady=20)

        timeLabel = Label(self, text="Time:   " + str(self.time))
        timeLabel.grid(column=1, row=4, sticky=tk.E, padx=5, pady=20)
        if self.count >= len(self.list):
            next_button["state"] = "disabled"

    def show_expanded(self):
        self.count = 0
        self.list = self.expanded_list


if __name__ == "__main__":
    bfs = BFS(State(125340678))
    found, explored, frontier, parents, run_time = bfs.search()
    app = App(list(reversed(bfs.goal_path)), explored, bfs.get_depth(), run_time)
    
    app.mainloop()
