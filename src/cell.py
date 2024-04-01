class Cell:
    
    def __init__(self, number) -> None:
        self.covered = True
        self.number = number
        self.flag = False
        self.mine = False
        # self.marked = False