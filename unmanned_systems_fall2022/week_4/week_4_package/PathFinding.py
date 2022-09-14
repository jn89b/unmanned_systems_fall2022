from week_4_package import Map, util_functions

import matplotlib.pyplot as plt

class Node():
    def __init__(self, x,y, cost, index) -> None:
        self.x = x
        self.y = y
        self.cost = cost
        self.index = int(index)
        
class Djikstras(object):
    def __init__(self, start:tuple, goal:tuple, 
                 move_list:list, configSpace:Map.ConfigSpace,
                 obs_radius  = 0.5) -> None:
        
        self.start = start
        self.goal  = goal
        self.visited_history = {}
        self.not_visited = {}
        self.move_list = move_list
        self.configSpace = configSpace
        
        if obs_radius != 0.5:
            self.obs_radius = obs_radius
        else:
            self.obs_radius = obs_radius
        
    def __init_search(self) -> Node:
        current_node = Node(self.start[0], self.start[1], 0, -1)
        current_node_index = self.configSpace.calc_index(self.start)
        self.not_visited[current_node_index ] = current_node

        return current_node

    def return_path(self, current_node:Node) -> list:
        path = []
        current = current_node
        
        while current.index != -1:
            #print("appending", current.index)
            #print("current index", current.index)
            path.append([current.x,current.y])
            current = self.visited_history[current.index]
        # Return reversed path as we need to show from start to end path
        path = path[::-1]
        start_value = 0
        waypoints = []
        for points in path:
            waypoints.append(points)
            
        return waypoints


    def find_path(self) -> list:
        current_node = Node(self.start[0], self.start[1], 0, -1)
        current_node_index = self.configSpace.calc_index(self.start)
        self.not_visited[current_node_index] = current_node
        
        while (current_node.x, current_node.y) != self.goal:
            current_node_index = min(self.not_visited, key=lambda x:self.not_visited[x].cost)
            current_node = self.not_visited[current_node_index]
            current_position = [current_node.x, current_node.y]

            self.visited_history[current_node_index] = current_node
            del self.not_visited[current_node_index]
        
            if (current_node.x, current_node.y)  == self.goal:
                ## have method to return path
                waypoints = self.return_path(current_node)
                print("path is found", waypoints)
                
                return waypoints

                
            for move in self.move_list:
                new_position = [current_position[0] + move[0], 
                                current_position[1] + move[1]]
                
                cost = current_node.cost + util_functions.compute_distance(
                                                    new_position, current_position)
                
                new_node = Node(new_position[0], new_position[1], cost, current_node_index)
                new_index = self.configSpace.calc_index(new_position)

                if self.configSpace.check_out_bounds(new_position) == True:
                    continue
                    
                #check within obstacle
                if self.configSpace.check_within_obstacle(
                        new_position, self.obs_radius) == True:
                    continue 

                if new_index in self.visited_history:
                    continue
                
                if new_index in self.not_visited:
                    if self.not_visited[new_index].cost > cost:
                        self.not_visited[new_index].cost  = cost
                        self.not_visited[new_index].index = current_node.index
                
                if new_index not in self.not_visited:           
                    self.not_visited[new_index] = new_node
                
class Astar(object):
    def __init__(self, start:tuple, goal:tuple, 
                 move_list:list, configSpace:Map.ConfigSpace,
                 obs_radius  = 0.5) -> None:
        
        self.start = start
        self.goal  = goal
        self.visited_history = {}
        self.not_visited = {}
        self.move_list = move_list
        self.configSpace = configSpace
        
        if obs_radius != 0.5:
            self.obs_radius = obs_radius
        else:
            self.obs_radius = obs_radius
        
    def return_path(self, current_node:Node) -> list:
        path = []
        current = current_node
        
        while current.index != -1:
            #print("appending", current.index)
            #print("current index", current.index)
            path.append([current.x,current.y])
            current = self.visited_history[current.index]
        # Return reversed path as we need to show from start to end path
        path = path[::-1]
        start_value = 0
        waypoints = []
        for points in path:
            waypoints.append(points)
            
        return waypoints


    def find_path(self) -> list:
        current_node = Node(self.start[0], self.start[1], 0, -1)
        current_node_index = self.configSpace.calc_index(self.start)
        self.not_visited[current_node_index ] = current_node
        
        while (current_node.x, current_node.y) != self.goal:
            
            """replace with priority queue"""
            current_node_index = min(self.not_visited, key=lambda x:self.not_visited[x].cost)
            current_node = self.not_visited[current_node_index]
            current_position = [current_node.x, current_node.y]

            self.visited_history[current_node_index] = current_node
            del self.not_visited[current_node_index]
        
            if (current_node.x, current_node.y)  == self.goal:
                ## have method to return path
                waypoints = self.return_path(current_node)
                print("path is found", waypoints)
                
                return waypoints

            for move in self.move_list:
                new_position = [current_position[0] + move[0], 
                                current_position[1] + move[1]]
                
                g_cost = util_functions.compute_distance(
                                                    new_position, current_position)
                
                h_cost = util_functions.compute_distance(
                                                    new_position, self.goal)
                
                cost = current_node.cost + g_cost + h_cost
                
                new_node = Node(new_position[0], new_position[1], cost, current_node_index)
                new_index = self.configSpace.calc_index(new_position)

                if self.configSpace.check_out_bounds(new_position) == True:
                    continue
                    
                #check within obstacle
                if self.configSpace.check_within_obstacle(
                        new_position, self.obs_radius) == True:
                    continue 

                if new_index in self.visited_history:
                    continue
                
                if new_index in self.not_visited:
                    if self.not_visited[new_index].cost > cost:
                        self.not_visited[new_index].cost  = cost
                        self.not_visited[new_index].index = current_node.index
                
                if new_index not in self.not_visited:           
                    self.not_visited[new_index] = new_node
                
        