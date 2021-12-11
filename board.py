from actor import Actor

# A child class of actor
class Board(Actor):
    def __init__(self):
        super().__init__()
        self._boardSize = 4
        self._board = []
        self.set_tag('board')

    # Creates an empty board
    def create_board(self):
        for i in range(self._boardSize):
            row = []
            for j in range(self._boardSize):
                row.append(0)
            self._board.append(row)

    # Getter for the board
    def get_board(self):
        return(self._board)

    # Getter for the board size
    def get_boardSize(self):
        return self._boardSize

    # Setter for the board
    def set_board(self, newBoard):
        self._board = newBoard

    # A different setter for the board using j i index.
    def set_board_byID(self, j, i, newNum):
        self._board[j][i] = newNum