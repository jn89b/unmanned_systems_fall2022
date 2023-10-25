"""
Djikstra's Pseudocode 

- Make two bins/dictionaries:
    - Unvisited 
    - Visited

- Initialize current_node with the following parameters:
    - position = start position
    - cost = 0
    - parent_index = -1
    
- initialize current_index by utilizing compute_index() function 
based on the current position, which is the start 

- insert current_node into unvisited dictionary, 
use the current_index as the key

- While current node position is not equal to goal location:
    - set current_index to min value from unvisited 
    - set current_node to unvisited[current_index]
    - put current_node into visited dictionary
    - delete current_index from unvisited 
    - check if current_node is equal to goal location:  
        - if so return path and break
        
    Begin search by doing th following:
    - Use get_all_moves() to get all moves based on current position
    - initialize a filtered_move list 
    - With all moves check if move is_not_valid by using is_not_valid() function
        - This function should check if:
            - Inside obstacle
            - Outside boundary 
            - Not on top of ourselves(already done by get_all moves)
        - If move is valid we append to filtered 
     
     - loop through all filtered moves:
        - based on this current filtered move:
        - calculate the filtered/new index
        - calculate the filtered/new cost
        - check if new index in visited:
            - continue if it is
        - check if new index is inside our unvisited:
            - if inside unvisited:
                - compare new_cost to unvisited cost:
                    - if new_cost < unvisited cost:
                        - update the cost value
                        - update the parent index 
                - continue
    
    - this last condition means that we have a node so 
        make a new node and append to unvisited
        
    

"""
import numpy as np
class Dog():
    def __init__(self, name=str):
        self.name = name

class Node():
    def __init__(self, 
                 x:float ,
                 y:float,
                 cost:float, 
                 parent_idx:int) -> None:
        self.x = x
        self.y = y 
        self.cost = cost
        self.parent_idx = int(parent_idx)



class Obstacle():
    def __init__(self, x_pos:float, y_pos:float, radius:float) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        
    def is_inside(self,curr_x:float, curr_y:float, 
                  robot_radius:float=0) -> bool:
        """
        Compute euclidean distance from current location -> obstacle locatin
        Store this value in a variable: dist_from 
        If dist_from > obstacle size:
                return false
        Otherwise return true
        """
        dist_from = np.sqrt((curr_x - self.x_pos)**2 + (curr_y - self.y_pos)**2)
        
        if dist_from > self.radius + robot_radius:
            return False
        
        return True


"""
    Writing functions Tips:
        - The way you to think of writing functions is: 
            - What are my inputs?
            - What are my outputs?
            
            - What will happen inside the blackbox/function?
            
    - is_not_valid_pos()
    - What are our inputs:?
        - Agent Position
        - Agent radius
        - Obstacles 
        - Obstacle radius 
        - x limits
        - y limits
        
    - What are our outputs:?
        - True/ False
        - True if not valid
        - False if valid
    
    - What will happen inside the blackbox/function?
        - Check if inside/near obstacles -> done 
        - Check if outside the boundary:
            - Check x pos:
                - Compare to x min and xmax 
                    - If x_min > x_pos: 
                        Return True
                    - If x_max < x_pos:
                        Return True
                - Do the same for y position

"""

def is_not_valid(obst_list:list, 
                 x_min:int, 
                 y_min:int, 
                 x_max:int, 
                 y_max:int,
                 x_curr:float, 
                 y_curr:float, 
                 agent_radius:float=0.0):
    """
    - True if not valid
    - False if valid
    
    - Check if inside/near obstacles -> done 
    - Check if outside the boundary:
        - Check x pos:
            - Compare to x min and xmax 
                - If x_min > x_pos: 
                    Return True
                - If x_max < x_pos:
                    Return True
            - Do the same for y position
    """
    
    # check if near obstacle or inside
    for obs in obst_list:
        if obs.is_inside(x_curr, y_curr,agent_radius):
            print("You're dead at ", obs.x_pos, obs.y_pos)
            return True
    
    if x_min > x_curr:
        return True
    if x_max < x_curr:
        return True
    if y_min > y_curr:
        return True
    if y_max < y_curr:
        return True

    return False
    

def get_all_moves(current_x:float, current_y:float, gs:float) -> list:
    """
    Inputs: 
        - current x and current y 
        - gridspace/step_size
        
    How should we do this:
        Hint a nested for loop helps and arange helps
    
    Returns a list of moves:
        - [[m1], [m2], [m3]..., [mn]]
    
    """
    
    move_list = []
    gs_x_bounds = np.arange(-gs, gs+gs, gs)
    gs_y_bounds = np.arange(-gs, gs+gs, gs)
    
    for dx in gs_x_bounds:
        for dy in gs_y_bounds:
            x_next = current_x + dx
            y_next = current_y + dy
            
            if [x_next, y_next] == [current_x, current_y]:
                continue
            
            move = [x_next, y_next]
            move_list.append(move)
            
    return move_list
             
    
#%% Example dictionary  - key: value 
# apa = Dog("apa")

# # to insert values into dictionary this is how you do it
# unvisited = {}
# unvisited["dog"] = 7
# unvisited["apa"] = apa

# # to check if something is in dictionary do this:
# # if "apa" in unvisited:
# #     print("yup he's here")
    
# if "goku" in unvisited:
#     print("yup he's here")
# else:
#     print("nope")

    
#%% Example of how to use the min dictionary
# unvisited = {}

# node1 = Node(0,0, 5, 7)
# node2 = Node(1,1, 2500, 10)
# node3 = Node(500, 100, 2, 99)

# unvisited[7] = node1
# unvisited[10] = node2
# unvisited[node3.parent_idx] = node3

# current_idx = min(unvisited, key=lambda x:unvisited[x].cost)

#%% Showing get all moves
x_curr = 0.5
y_curr = 0.5
gs = 0.5

min_x = 0
max_x = 10

min_y = 0
max_y = 10

gs = 0.5

obstacle_positions =  [(1,1), (4,4), (3,4), (5,0)]
obstacle_list = [] # store obstacle classes
obstacle_radius = 0.25

# Loop through position of obstacles
for obs_pos in obstacle_positions:
    obstacle = Obstacle(obs_pos[0], obs_pos[1], obstacle_radius)
    obstacle_list.append(obstacle)
    
agent_x = 1.5
agent_y = 1.5
agent_radius = 0.5

all_moves = get_all_moves(x_curr, y_curr, gs)

filtered_moves = []
for move in all_moves:
    if (is_not_valid(obstacle_list, min_x, min_y, max_x, max_y, 
                     move[0], move[1]) == True):
        continue
    else:
        print("good move", move[0], move[1])
    


