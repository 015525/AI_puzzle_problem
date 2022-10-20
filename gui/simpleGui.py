import tkinter as tk
from tkinter import ttk
from astar.solver import solver
from astar.heuristic.heuristic import manhattan
from astar.heuristic.heuristic import euclidian
from DFS.DFS import DFS
from state.State import State
class App(tk.Tk):
    count = 0

    def __init__(self, path_list, expanded2, depth2, time2):
        super().__init__()
        self.list = path_list
        self.path = path_list
        self.expanded_list = expanded2
        self.time = time2
        self.depth = depth2
        # root window
        self.geometry("400x500")
        self.title('path to goal')
        self.resizable(1, 1)
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

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
                cell = ttk.Label(self, text=display[index])
                cell.grid(column=j, row=i, padx=20, pady=50)
                index += 1

        next_button = ttk.Button(self, text="Next", command=self.create_widgets)
        next_button.grid(column=2, row=3, sticky=tk.E, padx=5, pady=20)

        expanded_button = ttk.Button(self, text="Expanded",
                                     command=lambda: [f() for f in [self.show_expanded, self.create_widgets]])
        expanded_button.grid(column=0, row=3, sticky=tk.E, padx=5, pady=20)

        depthLabel = ttk.Label(self, text="Depth:   " + str(self.depth))
        depthLabel.grid(column=0, row=4, sticky=tk.E, padx=5, pady=20)

        timeLabel = ttk.Label(self, text="Time:   " + str(self.time))
        timeLabel.grid(column=1, row=4, sticky=tk.E, padx=5, pady=20)
        if self.count >= len(self.list):
            next_button["state"] = "disabled"

    def show_expanded(self):
        self.count = 0
        self.list = self.expanded_list


if __name__ == "__main__":
    # a = solver()
    # path, expanded, depth, time = a.solve(142658730, manhattan())
    dfs = DFS(State(125340678))
    path, expanded, depth, time = dfs.run()
    print(path)
    app = App(path, expanded, depth, time)
    app.mainloop()
