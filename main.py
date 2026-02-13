from state import State
from utils import swap

def main():
    puzzle = State((1, 2, 3, 4, 0, 5, 6, 7, 8))
    puzzle.display()
    print(puzzle.blank)
    print(puzzle.get_neighbors())
    puzzle2 = puzzle.get_neighbors()
    puzzle2.display()
  




if __name__ == "__main__":
    main()