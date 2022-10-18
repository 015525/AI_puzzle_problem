
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
        self.cost = 1
        self.state = initial_state
        self.zero_place = self.get_zero_place(initial_state)

    def neighbours(self):
        #state = State(1234)
        #return state
        neighbour_states = []
        for i in self.allowed_ind_moves.get(self.zero_place):
            #print('iam in neighbours')
            desired_ind = self.total_puzzle_places-i-1
            #print('desired ind : ' + str(desired_ind))
            num = self.state % (10**(desired_ind+1))
            #print('num : ' + str(num))
            desired_num = int(num/(10**desired_ind))
            #print('desired num : ' + str(desired_num))
            desired_zero_place = self.total_puzzle_places - self.zero_place - 1
            new_num = self.state + (desired_num * (10 ** desired_zero_place))
            #print('new num first : ' + str(new_num))
            new_num = new_num - (desired_num * (10 ** desired_ind))
            #print('new num first : ' + str(new_num))
            state = State()
            state.state = new_num
            #print('state.state : ' + str(state.state))
            state.zero_place = i
            #print('state.zero_place : ' + str(state.zero_place))
            neighbour_states.append(state)
            #print('=========================================')

        return neighbour_states



    def get_zero_place(self, initial_state):
        if initial_state:
            #print("iam in get zero places")
            temp_state = initial_state
            temp = 10
            ind = -1
            while temp and ind != 8:
                ind += 1
                temp = temp_state%10
                temp_state = int(temp_state/10)

           # print(self.total_puzzle_places - ind - 1)
            return self.total_puzzle_places - ind - 1



#applying Breadth First Search algorithm
def BFS(start):
    frontier = [start.state] #queue to hold new nodes
     
    explored = [] #list to hold explored nodes
    
    parents = {start.state: start.state} #save each node to her parent node

    #while there is new node do BFS
    while(len(frontier) != 0):

        cur_state = State(frontier.pop(0)) #apply FIFO rule(first input node first out node)

        explored.append(cur_state.state) #the out node is explored
        
        #base case if the explored node is the goal node then return succesful 
        if(cur_state.state == 12345678):
            return True, explored, frontier

        #get node neighbours
        neighbours = cur_state.neighbours()

        #go through all the neighbours
        for i in neighbours:
            #add only the new node (wasn't explored or added to the frontier before) to the frontier
            if ((i.state not in frontier) and (i.state not in explored)):
                parents[i.state] =  cur_state.state #save new node parent
                frontier.append(i.state) 
                
    return False, [], [] #if the frontier is empty then the problem can't be solved


if __name__ == "__main__" :
    state = State(125340678)
    solvable, explore, frontier = BFS(state)
    print(f"is it solvable: {solvable}")
    print(f"explored values are: {explore}")
    print(f"frontier is are: {frontier}")
    #for s in state.neighbours() :
     #   print(s.state)
