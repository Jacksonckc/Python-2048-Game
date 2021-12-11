import random
from action import Action

class NewNumberAction(Action):
    def __init__(self,board):
        self._board = board

    def generate_new_num(self):
        chance = random.randint(1,20)
        if chance == 1:
            return 8
        elif chance == range(2, 8):
            return 4
        else:
            return 2

    def execute(self):
        

        numberNeeded = 2
        while numberNeeded > 0:
            rowNum = random.randint(0, self._board.get_boardSize() - 1)
            colNum = random.randint(0, self._board.get_boardSize() - 1)
        
            if self._board.get_board()[rowNum][colNum] == 0:
                self._board.set_board_byID(rowNum,colNum, self.generate_new_num())
                numberNeeded -= 1
