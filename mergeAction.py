

from action import Action


class MergeAction(Action):
    def __init__(self, board):
        self._board = board



    def execute(self, direction):
        if direction == 'a':
            self.mergeLeft()
        elif direction == 'd':
            self.mergeRight()
        elif direction == 'w':
            self.mergeUp()
        else:
            self.mergeDown()

    def mergeOneRowLeft(self, row):
        for j in range(self._board.get_boardSize() - 1):
            for i in range(self._board.get_boardSize()-1, 0, -1):
                if row[i - 1] == 0:
                    row[i-1] = row[i]
                    row[i] = 0

        for i in range(self._board.get_boardSize() - 1):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0

        for i in range(self._board.get_boardSize() - 1, 0, -1):
            if row[i - 1] == 0:
                row[i-1] = row[i]
                row[i] = 0
        return row

    def mergeLeft(self):
        tempBoard = [[], [], [], []]
        for i in range(self._board.get_boardSize()):
            tempBoard[i] = self.mergeOneRowLeft(self._board.get_board()[i])
        self._board.set_board(tempBoard)

    def reservse(self, row):
        tempRow = []
        for i in range(self._board.get_boardSize() - 1, -1, -1):
            tempRow.append(row[i])
        return tempRow

    def mergeRight(self):
        tempBoard = [[], [], [], []]
        for i in range(self._board.get_boardSize()):
            tempBoard[i] = self.reservse(self._board.get_board()[i])
            tempBoard[i] = self.mergeOneRowLeft(tempBoard[i])
            tempBoard[i] = self.reservse(tempBoard[i])

        self._board.set_board(tempBoard)

    def diagnolize(self):
        # curBoard = self._board.get_board()
        for j in range(self._board.get_boardSize()):

            for i in range(j, self._board.get_boardSize()):
                if i != j:

                    tempNum = self._board.get_board()[j][i]
                    self._board.set_board_byID(j, i, self._board.get_board()[i][j])
                    self._board.set_board_byID(i, j, tempNum)


    def mergeUp(self):

        self.diagnolize()
        self.mergeLeft()
        self.diagnolize()

    def mergeDown(self):

        self.diagnolize()
        self.mergeRight()
        self.diagnolize()
