import astar.aStar
from timeit import default_timer as timer
from state.State import State


class solver:

    def solve(self, initial_state, heuristic_type):
        state = State(initial_state)
        a = astar.aStar.Astar(heuristic_type)
        start = timer()
        print(a.a_star_search(state))
        end = timer()
        print("time =", end - start)
        self.get_path(initial_state, a)
        # self.get_expanded_nodes(a)
        self.get_max_depth(a)


    def get_path(self, initial_state, a):
        path = []
        temp = a.goal
        while True:
            path.append(temp)
            if temp == initial_state:
                break
            temp = a.parent_map[temp]

        print(path)
        print(len(path))

    def get_expanded_nodes(self, a):
        for i in a.expanded_nodes:
            print(i.state)

    def get_max_depth(self, a):
        return a.max_depth
