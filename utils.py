
def swap(State):
    new1 = list(State.board)

    new1[2] = 30

    return State(tuple(new1))
