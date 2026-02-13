
def main():
    ez_puzzle = (1,2,3,4,5,6,7,8,0)

    print(display(ez_puzzle))
    print(find_blank(ez_puzzle))

    for i in get_neighbors(ez_puzzle):
        print(display(i))





def find_blank(state):
        #get the row and column of the blank tile
        row = state.index(0) // 3
        col = state.index(0) % 3
        blank_index = state.index(0)
        return (row,col, blank_index)


def display(state):
    #this is for the 3x3 puzzle only right now
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])

def get_neighbors(state):
    neighbors = []
    row, col, blank_index = find_blank(state)

    if row > 0:
        new_blank = blank_index - 3
        new_state = swap(state, blank_index, new_blank)
        neighbors.append(new_state)

    return neighbors

def swap(state, index1, index2):
    temp = list(state)
    temp[index1], temp[index2] = temp[index2], temp[index1]

    return tuple(temp)

if __name__ == "__main__":
    main()