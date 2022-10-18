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
# print(State)
# p.put(comparable_state(State( 1)))
# p.put(comparable_state(State(  2)))
# p.put(comparable_state(State( 3)))
# print(p.get().state.cost)
# print(p.get().state.cost)
# print(p.get().state.cost)
# print(p.get().state.cost)


