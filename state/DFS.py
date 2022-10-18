import time
from State import State

class DFS:
    def __init__(self, initialState, goalStates):
        self.goal = None
        self.searchDepth = None
        self.initialState = initialState
        self.goalStates = goalStates
        self.parentMap = {}
        self.runTime = 0
        self.f = True
    def run(self):
        startTime = time.time()
        self.DFS()
        endTime = time.time()
        self.runTime = (endTime-startTime)

    def getRunTime(self):
        return self.runTime

    def goalState(self, state):
        for s in self.goalStates:
            if state == s.state:
                self.goal = s
                return True
        return False
    
    
    # get the path from start state to goal state
    def pathToGoalState(self):

        path = []                                       # list of path
        child = self.goal.state
        
        while True:
            if self.parentMap[child] == child:
                break
            
            else:
                path.append(self.parentMap[child])
                child = self.parentMap[child]
        path.reverse()
        self.searchDepth = len(path)
        print(len(path))
        return path

    def getSearchDepth(self):
        return self.searchDepth

    def nodesExpanded(self):
        return self.explored


    def DFS(self):
        
        frontire = []                                                       # Stack
        self.explored = set()                                               # explored states
        frontire.append(self.initialState)                                  # add initial state to stack
        self.parentMap[self.initialState.state] = self.initialState.state   # make initial state parent of it_self

        # loop over the stack
        while len(frontire) != 0:
            state = frontire.pop()
            self.explored.add(state.state)
            
            if self.goalState(state.state):                                 # DFS reach to goal state, all done
                print("DFS done")
                break
            
            neighbours = list(reversed(state.neighbours()))                                 # get all neighbours of the current state, sort them in reverse order
            for neighbour in neighbours:
                print(f"len of frontire = {len(frontire)}, and explored = {len(self.explored)}")
                if neighbour.state not in self.explored and neighbour not in frontire:
                    self.parentMap[neighbour.state] = state.state
                    frontire.append(neighbour)


dfs = DFS(State(125340678), [State(12345678)])
dfs.run()
print(dfs.getRunTime())
print(dfs.pathToGoalState())

# print(dfs.pathToGoalState())