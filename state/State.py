
class State:

    total_puzzle_places = 9
    allowed_ind_moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }

    def __init__(self, initial_state=0):
        self.cost = 0
        self.depth = 0
        self.state = initial_state
        self.zero_place = self.get_zero_place(initial_state)

    def neighbours(self):
        neighbour_states = []

        for i in self.allowed_ind_moves.get(self.zero_place):
            desired_ind = self.total_puzzle_places-i-1
            num = self.state % (10**(desired_ind+1))
            desired_num = int(num/(10**desired_ind))
            desired_zero_place = self.total_puzzle_places - self.zero_place - 1
            new_num = self.state + (desired_num * (10 ** desired_zero_place))
            new_num = new_num - (desired_num * (10 ** desired_ind))
            state = State()
            state.state = new_num
            state.zero_place = i
            neighbour_states.append(state)

        return neighbour_states

    def get_zero_place(self, initial_state):
        if initial_state:
            temp_state = initial_state
            temp = 10
            ind = -1
            while temp and ind != 8:
                ind += 1
                temp = temp_state%10
                temp_state = int(temp_state/10)
            return self.total_puzzle_places - ind - 1