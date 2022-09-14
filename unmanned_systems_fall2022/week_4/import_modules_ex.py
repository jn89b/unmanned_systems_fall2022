from week_4_package import Map, util_functions, PathFinding
from another_package import hello
import matplotlib.pyplot as plt

def plot_path(waypoints:list, configSpace:Map.ConfigSpace) -> plt:
    #plot the waypoints
    x_list = [x[0] for x in waypoints]
    y_list = [y[1] for y in waypoints]
    plt.plot(x_list, y_list)
    
    for obstacle in configSpace.obstacle_list:
        plt.scatter(obstacle[0], obstacle[1])
    
    return plt

if __name__ == '__main__':
    """set up config space"""
    x_span = [0,10]
    y_span = [0,10]
    grid_space = 0.5
    
    enemy_list = [(1,1), (4,4), (3,4), (5,0), (5,1), (0,7), (1,7), (2,7), (3,7)]
    configSpace = Map.ConfigSpace(x_span, y_span, grid_space, enemy_list)
    configSpace.set_graph_coords()
    obstacle_radius = 0.5
    
    """define start and end"""
    start_position = (0,0)
    goal_position = (8, 8)
    
    step_size = 1
    move_list = [[step_size,0], #move left
                [-step_size,0], #move right 
                [0,step_size], #move up
                [0,-step_size], #move down
                [step_size, step_size],
                [step_size, -step_size],
                [-step_size, step_size],
                [-step_size, -step_size]
                ]
    

    """instiantiate djikstras"""
    djikstras = PathFinding.Djikstras(start_position, goal_position, move_list,
                                      configSpace, obstacle_radius)
    
    path = djikstras.find_path()

    astar = PathFinding.Astar(start_position, goal_position, move_list,
                                      configSpace, obstacle_radius)
    
    astar_path = astar.find_path()
    
    hello.hello_world("Justin")
    
    #%% 
    plt.figure()

    x_list = [x[0] for x in path]
    y_list = [y[1] for y in path]
    plt.plot(x_list, y_list)
    
    for obstacle in configSpace.obstacle_list:
        plt.scatter(obstacle[0], obstacle[1])

    plt.show()

# %%
