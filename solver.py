import heapq

def main():
    #Get main input from user 1 for the trivial state. 2 for a custom state
    arg = int(input("Enter 1 for default trivial state, 2 for custom state: "))
    if arg == 1:
        currState = (1, 0, 2, 4, 5, 3, 7, 8, 6)
    elif arg == 2:
        custom_input = input("Enter the state as a list of 9 numbers (0 for blank tile), separated by spaces: ")
        currState = tuple(map(int, custom_input.split()))

    #goal state that will be compared against multiple times
    goal  = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    #this function checks the number of integers (pieces) for the puzzle and gets their number per column/row
    n = int(len(currState) ** 0.5)

    #print starting puzzle
    print("Starting State:\n")
    display(currState)

    #Main question asking the user for what algortihm they want to use
    alg = int(input("Enter 1 for Uniform Search Cost, 2 for A* with misplaced tile heuristic, 3 for A* with Manhattan distance heuristic: "))

    if alg == 1:
        a_star_search(currState, goal, zero_heuristic)
    elif alg == 2:
        a_star_search(currState, goal, misplaced_tile)
    elif alg == 3:
        a_star_search(currState, goal, manhattan_distance)
    else:
        print("Invalid input")



def a_star_search(start, goal, heuristic):
    #we want a priority queue that is (cost + heuristic, state, total cost))
    #initilaizing the priority queue and the visited set
    frontier = []
    heapq.heappush(frontier,(0 + heuristic(start,goal), start, 0))

    #will store what nodes or states we've seen already
    visited = set()

    #for tracking the path to the goal state later
    parent_path = {}
    parent_path[start] = None

    while (frontier):
        #popping values from the frontier
        currCost, state, totalCost = heapq.heappop(frontier)

        #if we've already seen it then continue
        if state in visited:
            continue
        
        #we've seen the state already 
        visited.add(state)

        #if we've already found the goal state then
        #calculate the path back to the start (see function)
        #then display the path we took from the start by steps
        if state == goal:
            path = path_to_goal(parent_path, goal)
            print("Solution found:")
            print(f"Number of moves: {len(path) - 1}")
            print(f"Nodes expanded: {len(visited)}")
            print("\nSolution path:")
            for step_num, step_state in enumerate(path):
                print(f"Step {step_num}:")
                display(step_state)
            return path
        
        #Expand the neighbors of each state. 
        #A neighbor is a state after a valid move of the blank
        #See the get_neighbors function for it's details
        #get_neighbors returns a list of all valid neighbors from the current state
        #We check if the valid neighbors are in the visited list then update our costs
        #Then push to the priority queue and display the neighbor and add the state to parent path
        for neighbor in get_neighbors(state):
                if neighbor not in visited:
                    new_totalCost = totalCost + 1
                    heuristic_cost = heuristic(neighbor, goal)
                    priorityCost = new_totalCost + heuristic_cost
                    heapq.heappush(frontier, (priorityCost, neighbor, new_totalCost))
                    print("Current heuristic: ", heuristic_cost)
                    print("Adding neighbor with cost: ", currCost + 1)
                    display(neighbor)
                    parent_path[neighbor] = state
        
    return None


#this funciton is used for Uniform cost search where we set the heuristic to 0
def zero_heuristic(state, goal):
    return 0


def misplaced_tile(state,goal):
    count = 0
    # we calculate the misplaced tile by counting how many tiles in the current state at index i
    # are not equal to the goal state at index i
    for i in range(len(state)):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def manhattan_distance(state,goal):
    distance = 0
    n = int(len(state) ** 0.5)

    #this function calculates total absolute value of the goal row - current row + goal column - current column

    for i in range(len(state)):
        if state[i] != 0:
            row, col = find_position(state, state[i])
            goalRow, goalCol = find_position(goal, state[i])
            distance += abs(goalRow - row) + abs(goalCol - col)
    return distance
    

def path_to_goal(parent_path, goal):
    path = []
    current = goal

    # to calculate the path back to the start node, we just follow the path back to the source
    # through the "parent_path" dictionary we created earlier 
    # by accessing the value (state) at the key (parent) then appending it to the path
    # then we update the current state to the next parent
    while current is not None:
        path.append(current)
        current = parent_path[current]

    # we have to reverse it because we have parent -> source but we need source -> parent
    path.reverse()
    return path

def find_blank(state):
        n = int(len(state) ** 0.5)
        #get the row and column of the blank tile
        row = state.index(0) // n
        col = state.index(0) % n
        return (row,col)

def find_position(state, tile):
    index = state.index(tile)
    n = int(len(state) ** 0.5)
    # return the row and column of any arbitrary tile
    row = index // n
    col = index % n
    return (row, col)

def display(state) -> None:
    #this is for the NxN puzzle now
    n = int(len(state) ** 0.5)
    for i in range(0, len(state), n):
        print(state[i:i+n])
    print("\n")

def get_neighbors(state):
    neighbors = []
    n = int(len(state) ** 0.5)
    row, col = find_blank(state)
    blank_index = state.index(0)


    #moving up
    if row > 0:
        new_blank = blank_index - n
        new_state = swap(state, blank_index, new_blank)
        neighbors.append(new_state)
    
    #moving down
    if row < n - 1:
        new_blank = blank_index + n
        new_state = swap(state, blank_index, new_blank)
        neighbors.append(new_state)
        
    #moving left
    if col > 0:
        new_blank = blank_index - 1
        new_state = swap(state, blank_index, new_blank)
        neighbors.append(new_state)

    #moving right
    if col < n - 1:
        new_blank = blank_index + 1
        new_state = swap(state, blank_index, new_blank)
        neighbors.append(new_state)
    return neighbors

def swap(state, index1, index2):
    temp = list(state)
    temp[index1], temp[index2] = temp[index2], temp[index1]

    return tuple(temp)

if __name__ == "__main__":
    main()