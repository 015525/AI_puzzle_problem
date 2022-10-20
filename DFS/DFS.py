import time
from state.State import State

class DFS:
    def __init__(self, initialState):
        self.goalState = 12345678
        self.initialState = initialState
        self.parentMap = {}
        self.runTime = 0

    def run(self):
        startTime = time.time()
        self.__DFS()
        endTime = time.time()
        self.runTime = (endTime-startTime)

        return self.pathToGoalState(), self.nodesExpanded(), self.getSearchDepth(), self.runTime

    # get the path from start state to goal state
    def pathToGoalState(self):
        # list of path
        path = []
        child = self.goalState
        path.append(child)
        while True:
            if self.parentMap[child] == child:
                break
            else:
                path.append(self.parentMap[child])
                child = self.parentMap[child]
        path.reverse()
        return path

    def getSearchDepth(self):
        depth = 0
        for i in self.nodes:
            depth = max(depth, self.explored[i])
        return depth

    def nodesExpanded(self):
        self.nodes = []
        for i in self.explored:
            self.nodes.append(i)
        return self.nodes

    def __DFS(self):
        # Stack
        frontire = []
        # explored states
        self.explored = {}
        # add initial state to stack
        frontire.append(self.initialState)
        # make initial state parent of it_self
        self.parentMap[self.initialState.state] = self.initialState.state
        # print(f'herhe      {self.parentMap[self.initialState.state]}')
        # loop over the stack
        while len(frontire) != 0:
            state = frontire.pop()
            self.explored[state.state] = state.depth
            # DFS reach to goal state, all done
            if state.state == self.goalState:
                print("DFS done")
                break
            # get all neighbours of the current state, sort them in reverse order
            neighbours = list(reversed(state.neighbours()))
            for neighbour in neighbours:
                # print(f"len of frontire = {len(frontire)}, and explored = {len(self.explored)}")
                if neighbour.state not in self.explored and neighbour not in frontire:
                    neighbour.depth = state.depth + 1
                    self.parentMap[neighbour.state] = state.state
                    frontire.append(neighbour)

if __name__ == "__main__":
    dfs = DFS(State(125340678))
    dfs.run()
    print(dfs.nodesExpanded())
    print(dfs.runTime)
    print(dfs.getSearchDepth())
