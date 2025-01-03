class Position:
    def __init__(self,id,name,description,possible_positions = None,item = None,):
        self.id = id
        self.name = name
        self.description = description
        self.item = item
        self.possible_positions = possible_positions
    