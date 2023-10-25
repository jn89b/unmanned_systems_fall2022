import numpy as np
import matplotlib.pyplot as plt

def compute_index(min_x:int, max_x:int, min_y:int, max_y:int,
                 gs:float, curr_x:int, curr_y:int) -> float:

    index = ((curr_x - min_x)/gs) + ((curr_y - min_y)/gs) * ((max_x+gs - min_x)/gs)
    
    return index

def improved_index(min_x:int, min_y:int, 
                  curr_x:int, curr_y:int, gs:int, x_size:int) -> float:
    
    index = ((curr_x - min_x)/gs) + ((curr_y - min_y)/gs) * x_size

    return index
 
if __name__ == '__main__':
    
    #%% 
    """
    This is Updating the Index equation
    """
    curr_x = 10
    curr_y = 10
    
    min_x = 0
    max_x = 10
    
    min_y = 0
    max_y = 10
    
    gs = 0.5
    
    index_val = compute_index(min_x, max_x, min_y, max_y,
                 gs, curr_x, curr_y)

    x_array = np.arange(min_x, max_x+gs, gs)
    
    improved_val = improved_index(min_x, min_y, 
                  curr_x, curr_y, gs, len(x_array))
    
    # value =  ((max_x+gs - min_x)/gs)

    print("old index", index_val)
    print("improved value", improved_val)
    
    # print("length of x array is", len(x_array))
    #%% 
    """
    
    HW 2 Problem 1
    
    Writing functions Tips:
        - The way you to think of writing functions is: 
            - What are my inputs?
            - What are my outputs?
            
            - What will happen inside the blackbox/function?
            
    For function to is_inside_obstacle(): 
        - What are inputs? 
            - Obstacle location [x,y] 
            - Obstacle size: radius
            - Current location [x,y]
        - What are our output(s)?
            - True/false
            - If inside: return true
            - If outside: return false
        - What will happen inside the blackbox
            - Compute euclidean distance from current location -> obstacle locatin
            - Store this value in a variable: dist_from 
            - If dist_from > obstacle size:
                return false
            - Otherwise return true
    
    """    
    
    def is_inside_obstacle(obs_x:float, obs_y:float, obs_radius:float, 
                          curr_x:float, curr_y:float) -> bool:
        """
        Compute euclidean distance from current location -> obstacle locatin
        Store this value in a variable: dist_from 
        If dist_from > obstacle size:
                return false
        Otherwise return true
        """
        
        dist_from = np.sqrt((curr_x - obs_x)**2 + (curr_y - obs_y)**2)
        
        if dist_from > obs_radius:
            return False
        
        return True
    
    #
    obs_x = 5
    obs_y = 5
    obs_radius = 4
    
    agent_x = 4 
    agent_y = 4
    
    if is_inside_obstacle(obs_x, obs_y, obs_radius, 
                          agent_x, agent_y):
        print("You're dead =(")
    else:
        print("You're okay =)")    

    # plot to visualize 
    # plot circle takes in a tuple of coorindates and radius
    agent_plot = plt.Circle((agent_x, agent_y), 0.5, color='red')
    obstacle_plot = plt.Circle((obs_x, obs_y), obs_radius, color='blue')
    
    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    ax.add_patch(obstacle_plot)
    #ax.scatter(agent_x, agent_y, c='r')
    ax.add_patch(agent_plot)
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)    
    plt.show()
    
    #%% 
    """
    Making the obstacle method better
    """
    
    class Obstacle():
        def __init__(self, x_pos:float, y_pos:float, radius:float) -> None:
            self.x_pos = x_pos
            self.y_pos = y_pos
            self.radius = radius
            
        def is_inside(self,curr_x:float, curr_y:float):
            """
            Compute euclidean distance from current location -> obstacle locatin
            Store this value in a variable: dist_from 
            If dist_from > obstacle size:
                    return false
            Otherwise return true
            """
            dist_from = np.sqrt((curr_x - self.x_pos)**2 + (curr_y - self.y_pos)**2)
            
            if dist_from > self.radius:
                return False
            
            return True
        
    some_obs = Obstacle(obs_x, obs_y, obs_radius)
    
    # check if obstacle is inside position
    if some_obs.is_inside(agent_x, agent_y):
        print("You're dead =(")
    else:
        print("You're okay =)")        

    
        

        
        
    