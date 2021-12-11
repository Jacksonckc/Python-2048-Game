from board import Board
from output import Output
from mergeAction import MergeAction
from getInputAction import GetInputAction 
from newNumberAction import NewNumberAction
from instruction import Instruction
from judge import Judge

class Director:
    def __init__(self):
        self.board = Board()
        self.output = Output()
        self.getInputAction = GetInputAction()
        self.newNumberAction = NewNumberAction(self.board)
        self.mergeAction = MergeAction(self.board)
        self.instruction = Instruction()
        self.judge = Judge()
        self.start_game()
    
    def start_game(self):
        self.instruction.create_start_instruction()
        self.output.display(self.instruction)
        self.board.create_board()

        while self.judge.get_game_status() == False:
            if self.judge.get_move_status() == False:
                self.newNumberAction.execute()  
            self.output.display(self.board)
            self.judge.set_temp_board(self.board)
            self.mergeAction.execute(self.getInputAction.execute())
            self.judge.if_no_moves(self.board)
            self.judge.determine_is_won(self.board)
            self.output.display(self.judge)
        self.output.display(self.board)
            


director = Director()