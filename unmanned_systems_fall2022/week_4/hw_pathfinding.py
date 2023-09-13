from pathfinding_lib.Node import Node
from pathfinding_lib.Obstacle import Obstacle
from pathfinding_lib.djikstra_astar import DjikstraAstar

# node = Node(0,0, -1, 0)

# print(node) 

# some_obs = Obstacle(2, 2, 5)

# #check if inside the obstacle works
# print(some_obs.is_inside(1,1))
# astar = DjikstraAstar()
# print(astar)


##### THIS IS HOW YOU SHOULD PROBABLY YOUR RUN HOMEWORK #################################
# initialize some parameters
start_x = 0
start_y = 0

min_x = 0
max_x = 10

min_y = 0
max_y = 10

goal_x = 7
goal_y = 7

gs = 0.5

obstacle_positions =  [(1,1), (4,4), (3,4), (5,0)]
obstacle_list = [] # store obstacle classes
obstacle_radius = 0.25

# Loop through position of obstacles
for obs_pos in obstacle_positions:
    obstacle = Obstacle(obs_pos[0], obs_pos[1], obstacle_radius)
    obstacle_list.append(obstacle)
    
astar = DjikstraAstar(True)
path = astar.find_path(start_x, start_y, min_x, min_y, max_x, max_y, goal_x, 
                goal_y, obstacle_list, gs)

print(path)




    
    
