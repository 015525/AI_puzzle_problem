import copy
from queue import PriorityQueue
from astar.priority import comparable_state
from astar.heuristic.heuristic import manhattan
from astar.heuristic.heuristic import euclidian


def decrease_key(frontier, state):
    temp_frontier = PriorityQueue()
    while not frontier.empty():
        temp = frontier.get()
        if temp.state.state == state.state and temp.state.cost > state.cost:
            temp_frontier.put(comparable_state(state))
            continue
        temp_frontier.put(temp)

    return copy.copy(temp_frontier)


class Astar:
    goal = 12345678
    parent_map = {}
    expanded_nodes = []
    max_depth = 0

    def __init__(self, heuristic_obj):
        self.frontier_states = set()
        self.heuristic_type = heuristic_obj

    def calculate_cost(self, state, cost):
        total = self.heuristic_type.cal(state)
        total += cost
        return total

    def goal_check(self, state):
        if state == self.goal:
            return True
        return False

    def in_frontier(self, state):
        state_num = state.state
        if state_num in self.frontier_states:
            return True
        return False

    def add_and_change(self, state, i):
        self.frontier_states.add(i.state)
        self.parent_map[i.state] = state.state

    def a_star_search(self, initial_state):
        self.calculate_cost(initial_state, 0)
        frontier = PriorityQueue()
        frontier.put(comparable_state(initial_state))
        self.frontier_states.add(initial_state.state)
        explored = set()
        while not frontier.empty():
            state = frontier.get().state
            self.frontier_states.remove(state.state)
            explored.add(state.state)
            self.expanded_nodes.append(state)

            if state.depth > self.max_depth:
                self.max_depth = state.depth

            if self.goal_check(state.state):
                return True

            for i in state.neighbours():
                if not self.in_frontier(i) and (i.state not in explored):
                    i.depth = state.depth + 1
                    i.cost = self.calculate_cost(i, i.depth)
                    frontier.put(comparable_state(i))
                    self.add_and_change(state, i)

                elif self.in_frontier(i):
                    i.depth = state.depth + 1
                    i.cost = self.calculate_cost(i, i.depth)
                    frontier = decrease_key(frontier, i)
                    self.add_and_change(state, i)

        return False
