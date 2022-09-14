import numpy as np
import math as m
from week_4_package import util_functions

class ConfigSpace():
    """
    sets up a configuration space based on the following inputs:
        x_bounds = [x_min,x_max]
        y_bounds = [y_min,y_max]
        spacing = grid spacing or step size in between values
    """
    def __init__(self, x_bounds:list, y_bounds:list, spacing:float,
                 obs_list=None) -> None:
        
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds
        self.spacing = spacing
        if obs_list != None:
            self.obstacle_list = obs_list
        
    def set_obstacles(self, obstacle_list:list) -> None:
        self.obstacles = obstacle_list
            
    def set_graph_coords(self) -> None:
        """graph coordinates and define the search space"""
        self.x_coords = np.arange(self.x_bounds[0], self.x_bounds[1]+self.spacing,
                                  self.spacing)
        
        self.y_coords = np.arange(self.y_bounds[0], self.y_bounds[1]+self.spacing,
                                  self.spacing)
        
        self.generate_search_space()
    
    def generate_search_space(self) -> None:
        """generate our search space"""
        self.search_space = np.zeros((len(self.x_coords),len(self.y_coords))) 
    
    def calc_index(self,position):
        """calculate index """
        index = (position[1] - self.y_bounds[0]) / \
            self.spacing * (self.x_bounds[1] - self.x_bounds[0] + self.spacing)/ \
                self.spacing + (position[0] - self.x_bounds[0]) / self.spacing
                
        return index            
    
    def check_within_obstacle(self, current_position:tuple, obs_radius:float) -> bool:
        """check if I am within collision of obstacle return True if it is
        false if I'm not"""        
        for obstacle in self.obstacle_list:
            distance = util_functions.compute_distance(current_position, obstacle)
            if abs(distance)<= obs_radius:
                return True
            
        return False
   
    def check_out_bounds(self, current_position:tuple) -> None:
        """check out of bounds of configuration space"""
        
        if current_position[0] < self.x_bounds[0] or current_position[0] > self.x_bounds[1]:
            return True
        
        if current_position[1] < self.y_bounds[0] or current_position[1] > self.y_bounds[1]:
            return True
        
        return False