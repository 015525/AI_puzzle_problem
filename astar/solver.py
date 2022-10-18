import astar.aStar
from timeit import default_timer as timer
from state.State import State


def get_path(initial_state, a):
    path = []
    temp = a.goal
    while True:
        path.append(temp)
        if temp == initial_state:
            break
        temp = a.parent_map[temp]

    path.reverse()
    return path


def get_expanded_states(a):
    lis = []
    for i in a.expanded_nodes:
        lis.append(i.state)
        print(i.state)
    return lis


def get_max_depth(a):
    return a.max_depth


class solver:

    def solve(self, initial_state, heuristic_type):
        state = State(initial_state)
        a = astar.aStar.Astar(heuristic_type)
        start = timer()
        print(a.a_star_search(state))
        end = timer()
        # print("time =", end - start)
        path = get_path(initial_state, a)
        ex = get_expanded_states(a)
        get_max_depth(a)
        return path, ex, a.max_depth, end - start
