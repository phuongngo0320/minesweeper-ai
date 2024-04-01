class Cell:
    
    def __init__(self, number) -> None:
        self.covered = True
        self.number = number
        self.flag = False
        self.mine = False
        # self.marked = False
        
    def check_input(self):
        if self.mine:
            return '*'
        
        # else: number
        return str(self.number)
        
    def __repr__(self) -> str:
        if self.covered:
            if self.flag:
                return '>'
            else:
                return '_'
            
        if self.mine:
            return '*'
        
        # else: number
        return str(self.number)
            
            