from actor import Actor


class Judge(Actor):
    def __init__(self):
        self._game_over = False
        self._tempBoard = []
        self.set_tag('instruction')
        self._instruction = ''
        self._no_moves = False
        self._is_won = False

    def get_game_status(self):
        return self._game_over

    def set_temp_board(self, board):
        self._tempBoard = board.get_board()

    def get_temp_board(self):
        return self._tempBoard

    def if_no_moves(self, board):
        if self._tempBoard == board.get_board():     
            self._instruction = 'Try a different direction!'
            self._no_moves = True
        else:
            self._instruction = 'Keep going!'
            self._no_moves = False

    def get_move_status(self):
        return self._no_moves

    def get_instruction(self):
        return self._instruction

    def determine_is_won(self, board):
        for row in board.get_board():
            if 2048 in row:
                self._is_won = True
                self._game_over = True
                self._instruction = 'You won!'