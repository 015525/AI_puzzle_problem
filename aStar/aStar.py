import copy
from queue import PriorityQueue
from astar.priority import comparable_state


def decrease_key(frontier, state):
    temp_frontier = PriorityQueue()
    while not frontier.empty():
        temp = frontier.get()
        if temp.state.state == state.state and temp.state.cost < state.cost:
            temp_frontier.put(comparable_state(state))
            continue
        temp_frontier.put(temp)

    return copy.copy(temp_frontier)


class Astar:
    goal = 12345678
    parent_map = {}
    expanded_nodes = []

    def __init__(self, heuristic_obj):
        self.frontier_states = set()
        self.heuristic_type = heuristic_obj

    def calculate_cost(self, state, cost=0):
        state.cost = self.heuristic_type.cal(state)
        state.cost += cost

    def goal_check(self, state):
        if state == self.goal:
            return True
        return False

    def in_frontier(self, state):
        state_num = state.state
        if state_num in self.frontier_states:
            return True
        return False

    def a_star_search(self, initial_state):
        self.calculate_cost(initial_state, 0)
        frontier = PriorityQueue()
        frontier.put(comparable_state(initial_state))
        self.frontier_states.add(initial_state.state)
        explored = set()

        gcost = 0

        while not frontier.empty():
            gcost += 1

            state = frontier.get().state
            self.frontier_states.remove(state.state)
            explored.add(state.state)
            self.expanded_nodes.append(state)

            if self.goal_check(state.state):
                return True

            for i in state.neighbours():
                self.calculate_cost(i, gcost)

                if (i.state not in self.frontier_states) and (i.state not in explored):
                    frontier.put(comparable_state(i))
                    self.frontier_states.add(i.state)
                    self.parent_map[i.state] = state.state
                    # print("parent", state.state, "child", i.state)

                elif self.in_frontier(i):
                    frontier = decrease_key(frontier, i)
                    self.frontier_states.add(i.state)
                    self.parent_map[i.state] = state.state
                    # print("parent", state.state, "child", i.state)

        return False
