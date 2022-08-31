

class Node():
    def __init__(self, parent:list, position:tuple) -> None:
        self.parent = parent
        self.position = position
        self.g = 0 
        self.h = 0
        self.f = 0
        self.cost = 0
        
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
    

# def is_valid(curr_position:list, obstacle_list:list, bounds:list) -> bool:
#     """check current position, if valid return True, else false"""
#     for obs in obstacle_list:
#         if curr_position within obs:
#             return False
        
#     for bound in bounds:
#         if curr_position out of out_bounds:
#             return False
        
#     return True
        


"""
Problem 1:
    - Input node position, obstacle list, and grid boudaries 
    - y = f(x), x are the inputs  
    - method should:
        run for loop inside obstacle list:
            check if current position within obstacle radius
            if is: 
                return some boolean 
            
        run for loop for boundaries:
            if out of boundary
                return some boolean
            
        example: is_valid -> return false is 
        
"""


#%%  How to loop through obstacles
obs_list = [(1,1), (4,4), (3,4), (5,0), (5,1), (0,7), (1,7), (2,7),(3,7)]

some_list = [2,2] # this is a mutable data structure
some_tuple = (2,2) # this is immutable

# for obs in obs_list:
#     print(obs)

"""
Class Example

"""

import numpy as np

class Djikstras():
    
    def __init__(self, x_bounds:list, y_bounds:list, obs_list:list, 
                 start:tuple, goal:tuple) -> None:
        """initialize and define attributes of Djikstras"""
        self.x_array = x_bounds 
        self.y_array = y_bounds
        self.obs_list = obs_list 
        self.goal = goal 
        self.start = start 
    
    # def is_valid(curr_position:list, obstacle_list:list, bounds:list) -> bool:
    #     """check current position, if valid return True, else false"""
    #     for obs in obstacle_list:
    #         if curr_position within obs:
    #             return False
            
    #     for bound in bounds:
    #         if curr_position out of out_bounds:
    #             return False
            
    #     return True    
    
    def is_valid(self, curr_position:list) -> bool:
        """check current position, if valid return True, else false"""
        curr_position = tuple(curr_position)
        for obs in self.obs_list:
            if curr_position == obs:
                return False
            
        # for bound in bounds:
        #     if curr_position in bound:
        #         return False
            
        return True



x_bounds = [0,10]
y_bounds = [0,10]
gs = 0.5

x_array = np.arange(x_bounds[0], x_bounds[1]+gs, 0.5)
y_array = np.arange(x_bounds[0], x_bounds[1]+gs, 0.5)

start_position = (0,1)
goal_position = (3,3)

djikstra = Djikstras(x_bounds, y_bounds, obs_list , start_position, goal_position)

## curr position is 1,1 so should return False
curr_position = [1,1]
is_valid = djikstra.is_valid(curr_position)
print("is valid is ", is_valid)


#%% If conditions 
c_r = 0.5
distance = 0.7 #from euclidian
if (c_r <= distance) and (c_r == distance):
    return True 

        
#%% Example for priority queue

# from queue import PriorityQueue

# class Node():
#     """
#     parent = parent of current node
#     posiition = position of node right now it will be x,y coordinates
#     g = cost from start to current to node
#     h = heuristic 
#     f = is total cost
#     """
#     def __init__(self, parent:list, position:list):
#         self.parent = parent 
#         self.position = position
        
#         self.g = 0
#         self.h = 0
#         self.f = 0
#         self.total_distance = 0
#         self.total_time = 0
        
#     def __lt__(self, other):
#         return self.f < other.f
    
#     # Compare nodes
#     def __eq__(self, other):
#         return self.position == other.position

#     # Print node
#     def __repr__(self):
#         return ('({0},{1})'.format(self.position, self.f))        
    
    
# node_small = Node(parent=[2,2,2], position=[3,3,3])
# node_small.f = 2


# node_big = Node(parent=[2,2,2], position=[3,3,3])
# node_big.f = 5

# prior_queue = PriorityQueue()
# prior_queue.put((node_big.f, node_big))
# prior_queue.put((node_small.f, node_small))

# val, some_node = prior_queue.get()







