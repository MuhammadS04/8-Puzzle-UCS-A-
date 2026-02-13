
def main():
    ez_puzzle = (1,2,3,4,5,6,7,8,0)

    print(display(ez_puzzle))

    print(find_blank(ez_puzzle))





def find_blank(state):
        #get the row and column of the blank tile
        row = state.index(0) // 3
        col = state.index(0) % 3
        return (row,col)


def display(state):
    #this is for the 3x3 puzzle only right now
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])


if __name__ == "__main__":
    main()