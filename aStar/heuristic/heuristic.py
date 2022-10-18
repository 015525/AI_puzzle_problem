import math


class manhattan:
    last_puzzle_x, last_puzzle_y = 2, 2

    def cal(self, state):
        temp_state = state.state
        total_remained_cost = 0
        for i in range(9):
            desired_num = temp_state % 10
            temp_state = int(temp_state / 10)
            curr_x, curr_y = self.last_puzzle_x - int(i / 3), self.last_puzzle_y - int(i % 3)
            goal_x, goal_y = int(desired_num / 3), int(desired_num % 3)
            total_remained_cost += abs(curr_x - goal_x) + abs(curr_y - goal_y)

        return total_remained_cost


class euclidian:

    last_puzzle_x, last_puzzle_y = 2, 2

    def cal(self, state):
        temp_state = state.state
        total_remained_cost = 0
        for i in range(9):
            desired_num = temp_state % 10
            temp_state = int(temp_state / 10)
            curr_x, curr_y = self.last_puzzle_x - int(i / 3), self.last_puzzle_x - int(i % 3)
            goal_x, goal_y = int(desired_num / 3), int(desired_num % 3)
            total_remained_cost += math.sqrt((curr_x - goal_x) ** 2 + (curr_y - goal_y) ** 2)

        return total_remained_cost

# if __name__ == "__main__":
#     aStar = heuristic()
#     print(aStar.manhattan_heuristic(310245678))
