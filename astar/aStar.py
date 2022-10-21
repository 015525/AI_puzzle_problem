from queue import PriorityQueue
from astar.priority import comparable_state


class Astar:
    goal = 12345678
    # Storing parent and child [child] -> parent
    parent_map = {}
    total_cost = 0
    expanded_nodes = []
    max_depth = 0

    def __init__(self, initial_state, heuristic_obj):
        # This set is used side by side with  frontier PQ in a a_star_search() 
        # to keep track of the states in frontier for fast access
        self.frontier_states = set()
        # Used to choose the type of heuristic the user wants the problem to use
        # 1) manhattan 2) euclidian
        self.heuristic_type = heuristic_obj
        self.initial_state = initial_state

    # Calculating total cost at certain node using f(n) = g(n) + h(n)
    def calculate_cost(self, state, cost):
        total = self.heuristic_type.cal(state)
        total += cost
        return total

    # Checking if we reached the goal
    def goal_check(self, state):
        if state == self.goal:
            return True
        return False

    # Checking if the state is in the frontier set 
    def in_frontier(self, state):
        state_num = state.state
        if state_num in self.frontier_states:
            return True
        return False

    # The method implementing A* search Algorithm
    def a_star_search(self):
        self.calculate_cost(self.initial_state, 0)
        frontier = PriorityQueue()

        frontier.put(comparable_state(self.initial_state))
        self.frontier_states.add(self.initial_state.state)
        explored = set()
        self.total_cost = self.initial_state.cost
        print(self.total_cost)
        while not frontier.empty():
            state = frontier.get().state
            # This means I have already checked this state with lower cost
            if not self.in_frontier(state):
                continue

            self.frontier_states.remove(state.state)
            explored.add(state.state)
            self.expanded_nodes.append(state)
            self.total_cost += state.cost

            if state.depth > self.max_depth:
                self.max_depth = state.depth

            if self.goal_check(state.state):
                return True

            # When a neighbour is already in frontier (maybe different cost)
            # I add it anyway to the frontier and the least cost will be expanded first
            # so, it will be removed from the set frontier (used to keep track of frontier states)
            # and then when I get that state again from the PQ I check if it not in the set 
            # then this implies the above is true and I have already expanded the same state
            # with different cost ,so I keep getting states objects from the PQ till I find
            # a one not expanded before
            for i in state.neighbours():
                if (not self.in_frontier(i) and (i.state not in explored)) or self.in_frontier(i):
                    i.depth = state.depth + 1
                    i.cost = self.calculate_cost(i, i.depth)
                    frontier.put(comparable_state(i))
                    self.frontier_states.add(i.state)
                    self.parent_map[i.state] = state.state

        return False

    def get_path(self):
        path = []
        temp = self.goal
        while True:
            path.append(temp)
            if temp == self.initial_state.state:
                break
            temp = self.parent_map[temp]

        path.reverse()
        return path

    def get_expanded_states(self):
        lis = []
        for i in self.expanded_nodes:
            lis.append(i.state)
        return lis

    def get_max_depth(self):
        return self.max_depth

