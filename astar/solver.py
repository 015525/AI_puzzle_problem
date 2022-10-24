from timeit import default_timer as timer
from state.State import State
from astar.heuristic.heuristic import manhattan
from astar.heuristic.heuristic import euclidian
import astar.aStar


def solve(initial_state, heuristic_type):
    obj = manhattan()
    if heuristic_type == "Euclidian":
        obj = euclidian()
    state = State(initial_state)
    a = astar.aStar.Astar(state, obj)
    start = timer()
    ans = a.a_star_search()
    end = timer()
    time = end - start
    # print("time =", end - start)
    
    if ans:
        path = a.get_path()
        ex = a.get_expanded_states()
        a.get_max_depth()
        return ans, ex, time, path, a.max_depth, a.optimal_cost
    return ans, [], time, [], a.max_depth, a.optimal_cost
