class OutOfRange(Exception):
    
    def __init__(self, r, c) -> None:
        super().__init__(f"Position ({r},{c}) is out of range")
    
    
class FlagUncovered(Exception):
    
    def __init__(self, r, c) -> None:
        super().__init__(f"Uncovering a flagged cell at ({r},{c})")
        
class FlagTwice(Exception):
    
    def __init__(self, r, c) -> None:
        super().__init__(f"Flagging a flagged cell at ({r},{c})")
    
class UncoverTwice(Exception):
    
    def __init__(self, r, c) -> None:
        super().__init__(f"Uncovering an uncovered cell at ({r},{c})")