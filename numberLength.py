
class NumberLength:
    def __init__(self):
        self._largestNumLength = 0

    def findTheLargestNumberLength(self, board):
        largest = board[0][0]
        
        for row in board:
            for number in row:
                if number > largest:
                    largest = number
            
        self._largestNumLength = len(str(largest))
    
    def get_largestNumLenghth(self):
        return self._largestNumLength

