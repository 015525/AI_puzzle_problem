import time

from state.State import State


class BFS:
    goal_state = 12345678  # const value(goal state)

    def __init__(self, start_state):
        self.parents = {start_state.state: start_state.state}  # save the parents of each state
        self.frontier = [start_state.state]  # queue to save each new state
        self.start_state = start_state  # the start state from the user
        self.goal_path = []  # save the final goal path
        self.explored = []  # save the explored states
        self.max_depth = 0

    def search(self):
        start_time = time.time()  # start calculating time

        while len(self.frontier) != 0:  # check all unexplored states

            cur_state = State(self.frontier.pop(0))  # apply FIFO rule(first input state first out state)
            self.explored.append(cur_state.state)  # current state is now explored

            if cur_state.state == self.goal_state:  # if the explored state is the goal state then return succesful
                end_time = time.time()  # end search time
                self.goal_path = self.get_goal_path()  # get the goal path(from start state to goal state)
                run_time = (end_time - start_time).__round__(10)  # calculate the run time
                return True, self.explored, run_time, list(reversed(self.goal_path)), self.get_depth(), self.get_cost()

            neighbours = cur_state.neighbours()  # get all neighbours states

            for i in neighbours:  # go through all the neighbours

                if ((i.state not in self.frontier) and (
                        i.state not in self.explored)):  # check if it's a new state(didn't show before)
                    self.parents[i.state] = cur_state.state  # save new node parent
                    self.frontier.append(i.state)  # add the new state to the queue

        # if there is no solution found
        end_time = time.time()  # end time of running
        run_time = (end_time - start_time).__round__(10)  # caclculate runtime
        return False, [], run_time, [], 0, 0  # if no solution return false and empty lists

    def get_depth(self):
        return len(self.goal_path) - 1

    def get_cost(self):
        return len(
            self.goal_path) - 1  # cost of each node = 1 (cost of the path = number of nodes in it -1 -->(the root
        # node))

    def get_goal_path(self):
        cur_state = self.goal_state  # start from end of the path
        self.goal_path.append(cur_state)  # save the path

        while cur_state != self.start_state.state:  # while we didn't reach the root node
            cur_state = self.parents.get(cur_state)  # move to the parent node
            self.goal_path.append(cur_state)  # save the new node

        return self.goal_path  # return final goal path


if __name__ == '__main__':
    bfs = BFS(State(125340678))
    found, explored, rtime, path = bfs.search()

    print(f"BFS done: {found}")
    print(f"we search for {len(explored)}")
    print(f"it took us {rtime} to find solution")
    print(f"the path of to the goal:")
    print(path)
