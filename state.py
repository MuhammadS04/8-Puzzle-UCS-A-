from utils import swap
class State:
    def __init__(self, board) -> None:
        self.board = board
        self.blank = self.board.index(0)

    def get_neighbors(self):
        neighbors = []

        #get the row and column of the blank tile
        row = self.blank // 3
        col = self.blank % 3

        new1 = swap(self)

        return new1

        #check if the move direction is valid and then do the move
        #check is done by checking if the row or column isn't at the end of the board

        #check : moving up
        # if row > 0:
        #     new_blank = self.blank - 3
        #     new_state = swap(self.board, self.blank, new_blank)
        #     neighbors.append(new_state)


    # def swap(self.board, index1, index2):
    #     temp = list(self.board)
    #     temp[index1], temp[index2] = temp[index2], temp[index1]

    #     return tuple(temp)


    def display(self):
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])
