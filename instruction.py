from actor import Actor


class Instruction(Actor):
    def __init__(self):
        super().__init__()
        self.set_tag('instruction')
        self._instruction = ''

    def create_start_instruction(self):
        self._instruction = 'Welcome to 2048! Your goal is to get to 2048 using the numbers appear on the board. You will have 2 randomly generated number each round, they could be 2, 4 or 8. Input a to merge left, d to merge right, w to merge up and s to merge down. Good luck!'

    def get_instruction(self):
        return self._instruction