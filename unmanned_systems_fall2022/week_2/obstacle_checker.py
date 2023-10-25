import numpy as np
import matplotlib.pyplot as plt


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

def is_not_valid(obst_list:list,x_min:int, y_min:int, x_max:int, y_max:int,
                 x_curr:float, y_curr:float, agent_radius:float=0.0):
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
    
    # if (x_min > x_curr) or (x_max < x_curr):
    #     return True

    return False
    
        
if __name__=='__main__':
    
    obstacle_positions =  [(1,1), (4,4), (3,4), (5,0)]
    obstacle_list = [] # store obstacle classes
    obstacle_radius = 0.25
    
    # Loop through position of obstacles
    for obs_pos in obstacle_positions:
        # print("obstacle_positions", obs_pos)
        #store obstacle information into obstacle list
        obstacle = Obstacle(obs_pos[0], obs_pos[1], obstacle_radius)
        obstacle_list.append(obstacle)
        
    agent_x = 1.5
    agent_y = 1.5
    agent_radius = 0.5
    
    #check obstacle collision    
    for obs in obstacle_list:
        print("This obstacles position is", obs.x_pos, obs.y_pos)
        if obs.is_inside(agent_x, agent_y,agent_radius):
            print("You're dead at ", obs.x_pos, obs.y_pos)
            break


    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)    
    for obs in obstacle_list:
        obs_plot = plt.Circle((obs.x_pos, obs.y_pos), obs.radius, color='blue')
        ax.add_patch(obs_plot)
    
    agent_plot = plt.Circle((agent_x, agent_y), agent_radius, color='red')
    ax.add_patch(agent_plot)
    plt.show()

    # # plot to visualize 
    # # plot circle takes in a tuple of coorindates and radius
    # agent_plot = plt.Circle((agent_x, agent_y), 0.5, color='red')
    # obstacle_plot = plt.Circle((obs_x, obs_y), obs_radius, color='blue')
    
    # fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    # ax.add_patch(obstacle_plot)
    # #ax.scatter(agent_x, agent_y, c='r')
    # ax.add_patch(agent_plot)

    # plt.show()
        

            
            

        
    