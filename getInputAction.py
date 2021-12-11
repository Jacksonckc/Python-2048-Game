from action import Action

class GetInputAction(Action):
    def __init__(self):
        self._direction = None
        self.vaildInput = False

    def execute(self):
        self.vaildInput = False
        while self.vaildInput == False:
            self._direction = input('What do you want to merge?')
            if self._direction == 's' or self._direction == 'w' or self._direction == 'a' or self._direction == 'd':
                self.vaildInput = True
            else: 
                print('Invalid input, try again please')
        return self._direction