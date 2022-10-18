import time
class DFS:
    def __init__(self, initialState, goalStates):
        self.initialState = initialState
        self.goalStates = goalStates
        self.parentMap = [{}]
        self.runTime = 0

    def run(self):
        startTime = time.time()
        self.DFS()
        endTime = time.time()
        self.runTime = (endTime-startTime).__round__(10)

    def getRunTime(self):
        return self.runTime

    def goalState(self, state):
        for s in self.goalStates:
            if state.state == s.state:
                self.goal = s
                return True
        return False
    # get the path from start state to goal state
    def pathToGoalState(self):
        # list of path
        path = []
        child = self.goal
        for dict in self.parentMap:
            path.append(dict[child])
            child = dict[child]
        path.reverse()
        self.searchDepth = len(path)
        return path

    def getSearchDepth(self):
        return self.searchDepth
    def nodesExpanded(self):
        return self.explored

    def DFS(self):
        # Stack
        frontire = []
        # explored states
        self.explored = set()
        # add initial state to stack
        frontire.append(self.initialState)
        # make initial state parent of it_self
        self.parentMap.append({self.initialState.state: self.initialState.state})
        # loop over the stack
        while len(frontire) != 0:
            state = frontire.pop()
            self.explored.add(state.state)
            # DFS reach to goal state, all done
            if self.goalState(state):
                print("DFS done")
                break
            # get all neighbours of the current state, sort them in reverse order
            neighbours = state.neighbours().sort(reverse=True)
            for neighbour in neighbours:
                if neighbour.state not in self.explored and neighbour not in frontire:
                    self.parentMap.append({neighbour.state: state.state})
                    frontire.append(neighbour.state)
