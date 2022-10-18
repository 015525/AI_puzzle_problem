import astar.aStar
from astar.heuristic.heuristic import manhattan
from astar.heuristic.heuristic import euclidian
from state.State import State


class solver:

    def solve(self, initial_state):
        state = State(initial_state)
        a = astar.aStar.Astar(manhattan())
        print(a.a_star_search(state))
        self.get_path(initial_state, a)
        self.get_expanded_nodes(a)

    def get_path(self, initial_state, a):
        path = []
        temp = a.goal
        while True:
            path.append(temp)
            if temp == initial_state:
                break
            temp = a.parent_map[temp]

        print(path)

    def get_expanded_nodes(self, a):
        for i in a.expanded_nodes:
            print(i.state)
