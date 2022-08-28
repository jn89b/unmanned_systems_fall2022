class Node():
    def __init__(self, parent:list, position:tuple) -> None:
        self.parent = parent
        self.position = position
        self.g = 0 
        self.h = 0
        self.f = 0
        
    # compare nodes greater
    def __lt__(self, other) -> bool:
        return self.f < other.f

    # Compare nodes
    def __eq__(self, other) -> bool:
        return self.position == other.position

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))
        

def print_hello(input:str) -> str:
    return "hello " + str(input)
    

