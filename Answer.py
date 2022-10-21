from tkinter import *
import tkinter as tk

from AI_puzzle_problem.BFS.BFS import BFS
from AI_puzzle_problem.exploration import Explore
from AI_puzzle_problem.state.State import State


class mainAnswer(tk.Tk):
    count = 0

    def __init__(self, goal_path, explored_states, depth, cost, rtime):
        super().__init__()
        self.path_to_goal = goal_path           # path to goal
        self.explored_list = explored_states    # explored states during search
        self.cost = cost                        #cost of search
        self.time = rtime                        #run time needed during the search
        self.depth = depth                      #the depth of the tree

        # root window
        self.config(bg='orange')
        self.geometry("400x500")
        self.title('path to goal')
        self.resizable(1, 1)
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_widgets()


    def create_widgets(self):
        num = self.path_to_goal[self.count]
        display = str(num)
        if len(display) == 8:
            display = "0" + display

        index = 0
        for i in range(3):
            for j in range(3):
                t = ""
                if(display[index] != '0'):
                    t = display[index]

                cell = Label(self, text=t, font=("Arial", 15), height=3, width=20)
                cell.grid(column=j, row=i, padx=3, pady=3)
                index += 1

        next_button = Button(self, text="Next", font=("Arial", 15), command=self.next_state)
        next_button.grid(column=2, row=3, padx=5, pady=20)

        explored = Button(self, text="explored", font=("Arial", 15), command=self.show_expanded)
        explored.grid(column=1, row=3, padx=5, pady=20)

        previous = Button(self, text="previous", font=("Arial", 15), command=self.previous_state)
        previous.grid(column=0, row=3, padx=5, pady=20)

        depthLabel = Label(self, text="Depth: " + str(self.depth), font=("Arial", 15))
        depthLabel.grid(column=0, row=4, padx=3, pady=20)

        timeLabel = Label(self, text="Time: " + str(self.time), font=("Arial", 15))
        timeLabel.grid(column=1, row=4, padx=3, pady=20, columnspan=2)

        path = Label(self, text="path: " + str(self.count + 1) + "\\" + str(len(self.path_to_goal)), font=("Arial", 15))
        path.grid(column=0, row=5, padx=3, pady=10)

        explored = Label(self, text="explored: " + str(len(self.explored_list)), font=("Arial", 15))
        explored.grid(column=1, row=5, padx=3, pady=10, columnspan=2)

        cost = Label(self, text="cost: " + str(self.cost), font=("Arial", 15))
        cost.grid(column=0, row=6, padx=3, pady=10)

        back = Button(self, text="back to main", font=("Arial", 15), bg='grey', command=self.return_to_main)
        back.grid(column=1, row=6, padx=3, pady=3, columnspan=2)

        if self.count >= (len(self.path_to_goal) - 1):
            next_button["state"] = "disabled"

        if self.count <= 0:
            previous["state"] = "disabled"

    def show_expanded(self):
        window = Explore(self.explored_list)

    def next_state(self):
        self.count += 1
        self.create_widgets()

    def previous_state(self):
        self.count -= 1
        self.create_widgets()

    def return_to_main(self):
        self.destroy()


if __name__ == '__main__':
    bfs = BFS(State(125340678))
    found, explored, time, path = bfs.search()

    win = mainAnswer(path, explored, bfs.get_depth(), bfs.get_cost(), time)
    win.mainloop()
