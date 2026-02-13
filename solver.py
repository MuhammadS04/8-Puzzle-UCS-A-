import heapq

def main():
    currState = (1, 0, 2, 4, 5, 3, 7, 8, 6)
    goal  = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    print(currState.index(0))

    display(currState)
    #print(find_blank(ez_puzzle))

    # for i in get_neighbors(currState):
    #     print("Neighbor:")
    #     display(i)
    
    print(misplaced_tile_hueristic(currState,goal))
    print(manhattan_distance(currState,goal))

    uniform_cost_search(currState, goal)


def a_star_search(start, goal):
    #we want a priority queue that is (cost + heuristic, state)
    #initilaizing the priority queue and the visited set
    #pritioty queue will be (cost, state)
    frontier = []
    heapq.heappush(frontier,(0, start))

    visited = set()

def uniform_cost_search(start, goal):
        #initilaizing the priority queue and the visited set
        #pritioty queue will be (cost, state)
        frontier = []
        #push the initial state with cost 0 so we have something to work off of 
        heapq.heappush(frontier, (0, start))
        visited = set()

        while (frontier):
            currCost, state = heapq.heappop(frontier)
            if state in visited:
                continue
            visited.add(state)
            if state == goal:
                print("Found the solution with current cost: ", currCost)
                return state
            for i in get_neighbors(state):
                heapq.heappush(frontier, (currCost + 1, i))
                print("Adding neighbor with cost: ", currCost + 1)
                display(i)
            
        return None



def find_blank(state):
        #get the row and column of the blank tile
        row = state.index(0) // 3
        col = state.index(0) % 3
        return (row,col)

def find_position(state, tile):
    index = state.index(tile)
    row = index // 3
    col = index % 3
    return (row, col)

def display(state) -> None:
    #this is for the 3x3 puzzle only right now
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print("\n")

def get_neighbors(state):
    neighbors = []
    row, col = find_blank(state)
    blank_index = state.index(0)


    #moving up
    if row > 0:
        new_blank = blank_index - 3
        new_state = swap(state, blank_index, new_blank)
        neighbors.append(new_state)
    
    #moving down
    if row < 2:
        new_blank = blank_index + 3
        new_state = swap(state, blank_index, new_blank)
        neighbors.append(new_state)
        
    #moving left
    if col > 0:
        new_blank = blank_index - 1
        new_state = swap(state, blank_index, new_blank)
        neighbors.append(new_state)

    #moving right
    if col < 2:
        new_blank = blank_index + 1
        new_state = swap(state, blank_index, new_blank)
        neighbors.append(new_state)
    return neighbors

def swap(state, index1, index2):
    temp = list(state)
    temp[index1], temp[index2] = temp[index2], temp[index1]

    return tuple(temp)

def misplaced_tile_hueristic(state,goal):
    count = 0
    for i in range(len(state)):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def manhattan_distance(state,goal):
    distance = 0
    for i in range(len(state)):
        if state[i] != 0:
            row, col = find_position(state, state[i])
            goalRow, goalCol = find_position(goal, state[i])
            distance += abs(goalRow - row) + abs(goalCol - col)
    return distance
    


if __name__ == "__main__":
    main()