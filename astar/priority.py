from queue import PriorityQueue
from state.State import State


class comparable_state:

    def __init__(self, state):
        self.state = state

    def __gt__(self, other):
        return self.state.cost > other.state.cost

    def __eq__(self, other):
        return self.state.cost == other.state.cost

    def __repr__(self):
        return repr(self.state)


# p = PriorityQueue()
# k = State(1)
# k.cost = 3
# p.put(comparable_state(k))
# n = State(1)
# n.cost = 4
# p.put(comparable_state(n))
# f = State(1)
# f.cost = 6
# p.put(comparable_state(f))
# print(p.get().state.cost)
# print(p.get().state.cost)
# print(p.get().state.cost)
# print(p.get().state.cost)


