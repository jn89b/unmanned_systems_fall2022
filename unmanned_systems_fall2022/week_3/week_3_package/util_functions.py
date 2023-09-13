import math as m

def add(x:float, y:float)-> float:
    return x + y 

def compute_distance(current_pos, another_pos):
    """compute distance"""
    return m.dist(current_pos, another_pos)
