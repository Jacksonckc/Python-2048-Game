# Parent class for all the actors, tag will chagne in each child class

class Actor:
    def __init__(self):
        self._tag = ''

    # Tag setter
    def set_tag(self, tag):
        self._tag = tag

    # Tag getter
    def get_tag(self): 
        return self._tag
    

    