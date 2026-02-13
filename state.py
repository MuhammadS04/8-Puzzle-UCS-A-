class State:
    def __init__(self, board) -> None:
        self.board = board
        self.zero_pos = self.board.index(0)

    #def get_neighbors(self):


    def display(self):
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])
