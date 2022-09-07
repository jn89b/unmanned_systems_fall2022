# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 21:16:09 2022
Lab 3 Excerise

1. Set up config space
- Make sure obstacles are there
- Check if obstacles can be detected

2. Make Turtle
- have set moves and use move
- keep track of what it sees 
- keep track of path history

3. Begin to navigate
- start turtle at some location
- begin moving upward 
- if out of bounds no go 
- if object is seen move left or right 

"""

import numpy as np
from math import dist
import matplotlib.pyplot as plt

class Node():
    def __init__(self, x,y, cost, index):
        self.x = x
        self.y = y
        self.cost = cost
        self.index = int(index)

class Turtle():
    def __init__(self, x, y, step_size):
        self.position  = [x,y]
        self.move_list = [[step_size,0], #move left
                          [-step_size,0], #move right 
                          [0,step_size], #move up
                          [0,-step_size], #move down
                          [step_size, step_size],
                          [step_size, -step_size],
                          [-step_size, step_size],
                          [-step_size, -step_size]
                          ]
        
        self.visited_history = {}
        self.not_visited = {} 
        self.obstacle_location = {}
        
    def teleport(self, new_position):
        """teleports if it sees obstacle"""
        return [new_position[0] + 0,
                new_position[1] + 1*2]
    
class ConfigSpace():
    """
    sets up a configuration space based on the following inputs:
        x_bounds = [x_min,x_max]
        y_bounds = [y_min,y_max]
        spacing = grid spacing or step size in between values
    """
    def __init__(self, x_bounds, y_bounds, spacing):
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds
        self.spacing = spacing
        
    def set_obstacles(self, obstacle_list):
        self.obstacles = obstacle_list
            
    def set_graph_coords(self):
        """graph coordinates and define the search space"""
        self.x_coords = np.arange(self.x_bounds[0], self.x_bounds[1]+self.spacing,
                                  self.spacing)
        
        self.y_coords = np.arange(self.y_bounds[0], self.y_bounds[1]+self.spacing,
                                  self.spacing)
        
        self.generate_search_space()
    
    def generate_search_space(self):
        """generate our search space"""
        self.search_space = np.zeros((len(self.x_coords),len(self.y_coords))) 
    
    def set_graph_nodes(self):
        """set graph index based on some index val"""
     
    def place_obstacles(self, obst_list):
        """places obstacles in grid by inserting a 1""" 
        for obstacle in obst_list:
            obs_x = obstacle[0]
            obs_y = obstacle[1]
            self.search_space[obs_x, obs_y]= 1
    
    def calc_index(self,position):
        """calculate index """
        index = (position[1] - self.y_bounds[0]) / \
            self.spacing * (self.x_bounds[1] - self.x_bounds[0] + self.spacing)/ \
                self.spacing + (position[0] - self.x_bounds[0]) / self.spacing
                
        return index            
    
    def check_within_obstacle(self, obstacle_list, current_position, obs_radius):
        """check if I am within collision of obstacle return True if it is
        false if I'm not"""
        for obstacle in obstacle_list:
            distance = compute_distance(current_position, obstacle)
            if abs(distance)<=obstacle_radius:
                return True
            
        return False
   
    def check_out_bounds(self, current_position, x_bounds, y_bounds):
        """check out of bounds of configuration space"""
        
        if current_position[0] < self.x_bounds[0] or current_position[0] > self.x_bounds[1]:
            return True
        
        if current_position[1] < self.y_bounds[0] or current_position[1] > self.y_bounds[1]:
            return True
        
        return False

def check_obstacle_exists(obstacle_list):
    """sanity check to see if obstacle exists"""
    for obst in obstacle_list:
        if configSpace.search_space[obst[0],obst[1]] == 1:
            print("yes", configSpace.search_space[obst[0],obst[1]])
    
def compute_distance(current_pos, another_pos):
    """compute distance"""
    return dist(current_pos, another_pos)
        
def return_path(current_node, turtle):
    path = []
    current = current_node
    
    while current.index != -1:
        #print("appending", current.index)
        #print("current index", current.index)
        path.append([current.x,current.y])
        current = turtle.visited_history[current.index]
    # Return reversed path as we need to show from start to end path
    path = path[::-1]
    start_value = 0
    waypoints = []
    for points in path:
        waypoints.append(points)
        
    return waypoints

if __name__=='__main__':
    #set up parameters
    x_span = [0,10]
    y_span = [0,10]
    spacing = 0.5
    
    
#%% ##### BUILD WORLD
    configSpace = ConfigSpace(x_span, y_span, spacing)
    configSpace.set_graph_coords()
    #(1,1), (4,4), (3,4), (5,0), (5,1), (0,7), (1,7), (2,7), and (3,7)
    enemy_list = [[1,1], [4,4], [3,4], [5,0], [5,1], [0,7], [1,7], [2,7], [3,7]]
    configSpace.set_obstacles(enemy_list)
    
    obstacle_radius = 0.5
    
#%% Build Turtlebot
    turtle = Turtle(0,0,spacing)
    goal_position = [8,9]

    current_node = Node(turtle.position[0], turtle.position[1], 0, -1)
    current_node_index = configSpace.calc_index(turtle.position)
    turtle.not_visited[current_node_index ] = current_node
    
    while [current_node.x, current_node.y] != goal_position:
    
        current_node_index = min(turtle.not_visited, key=lambda x:turtle.not_visited[x].cost)
        current_node = turtle.not_visited[current_node_index]
        turtle.position = [current_node.x, current_node.y]

        print("turtle position is", turtle.position)
        turtle.visited_history[current_node_index] = current_node
        del turtle.not_visited[current_node_index]
    
        if [current_node.x, current_node.y]  == goal_position:
            ## have method to return path
            print("I've arrived!", current_node.x, current_node.y)
            waypoints = return_path(current_node, turtle)
            
            #plot the waypoints
            x_list = [x[0] for x in waypoints]
            y_list = [y[1] for y in waypoints]
            plt.plot(x_list, y_list)
            
            for obstacle in enemy_list:
                plt.scatter(obstacle[0], obstacle[1])
            
            break
    
        for move in turtle.move_list:
            new_position = [turtle.position[0] + move[0], 
                            turtle.position[1] +move[1]]
            
            print("new position", new_position)
            cost = current_node.cost + compute_distance(new_position, turtle.position)
            new_node = Node(new_position[0], new_position[1], cost, current_node_index)
            new_index = configSpace.calc_index(new_position)

            if configSpace.check_out_bounds(new_position, x_span, y_span) == True:
                print("you are out of bounds", new_position)
                continue
                
            #check within obstacle
            if configSpace.check_within_obstacle(
                    enemy_list, new_position, obstacle_radius) == True:
                continue 
            

            if new_index in turtle.visited_history:
                continue
            
            if new_index in turtle.not_visited:
                if turtle.not_visited[new_index].cost > cost:
                    turtle.not_visited[new_index].cost  = cost
                    turtle.not_visited[new_index].index = current_node.index
            
            if new_index not in turtle.not_visited:           
                turtle.not_visited[new_index] = new_node
            
        
        