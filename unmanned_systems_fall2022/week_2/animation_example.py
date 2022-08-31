# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:15:34 2022

@author: jnguy
"""



#% Import stuff here
import seaborn as sns 
import matplotlib as plt


from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation

#% Classes 




#% Main 

class AnimateMultiUAS():
    def __init__(self, uas_paths:list, method_name:str):
        self.uas_paths = uas_paths
        self.method_name = method_name
        self.color_list = sns.color_palette("hls", len(uas_paths))
        self.bad_index = [] #bad indexes are index locations where paths cant be found
        
    def set_size_params(self,x_bounds:list, y_bounds:list, 
                        z_bounds:list):
        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_xlim3d(x_bounds[0], x_bounds[1])
        self.ax.set_ylim3d(y_bounds[0], y_bounds[1])
        self.ax.set_zlim3d(z_bounds[0], z_bounds[1])
        self.title = self.ax.set_title(self.method_name,fontsize=18)

    def plot_initial_final(self, start_pos, goal_pos, color):
        """plots the initial and final points of a UAS with a color"""
        self.graph = self.ax.scatter(start_pos[0], start_pos[1],
                        start_pos[2], color=color, s=100, marker='o')
        
        self.graph = self.ax.scatter(goal_pos[0], goal_pos[1], 
                        goal_pos[2], color=color, s=100, marker='x')
        
        return self.graph

    def init(self):
        for line, pt in zip(self.lines, self.pts):
            line.set_data([], [])
            line.set_3d_properties([])

            pt.set_data([], [])
            pt.set_3d_properties([])
        return self.lines + self.pts

    def update_multi(self,i:int):
        # we'll step two time-steps per frame.  This leads to nice results.
        # i = (2 * i) % x_t.shape[0]

        # for line, pt, xi in zip(lines, pts, x_t):
        for j, (line,pt) in enumerate(zip(self.lines,self.pts)):
            time_span = 1
            if i < time_span:
                interval = 0
            else:
                interval = i - time_span
            
            #set lines 
            line.set_data(self.x_list[j][:i], self.y_list[j][:i])
            line.set_3d_properties(self.z_list[j][:i])

            # #set points
            pt.set_data(self.x_list[j][interval:i], self.y_list[j][interval:i])
            pt.set_3d_properties(self.z_list[j][interval:i])
        
            #changing views
            # self.ax.view_init(60, 0.3 * i)
            # self.fig.canvas.draw()
            
        # fig.canvas.draw()
        return self.lines + self.pts
    

    def animate_multi_uas(self, x_bounds:list, y_bounds:list, z_bounds:list, 
                            axis_on=True, save=False):
        """animate and simulate multiple uas"""
        #https://stackoverflow.com/questions/56548884/saving-matplotlib-animation-as-movie-movie-too-short
        #marker_size = 80
        self.set_size_params(x_bounds, y_bounds, z_bounds)
        
        if axis_on == False:
            self.ax.axis("off")
        
        self.x_list = []
        self.y_list = []
        self.z_list = []
        
        for i, uav_path in enumerate(self.uas_paths):
            
            #checking if we have a path
            if not uav_path:
                self.bad_index.append(i)
            else:
                self.curr_color = self.color_list[i]
                x_list = [position[0] for position in uav_path]
                y_list = [position[1] for position in uav_path]
                z_list = [position[2] for position in uav_path]
                
                start_pos = [x_list[0], y_list[0], z_list[0]]
                goal_pos  = [x_list[-1], y_list[-1], z_list[-1]]
                
                self.graph = self.plot_initial_final(start_pos, 
                                                        goal_pos, 
                                                        self.color_list[i])         
            
                self.x_list.append(x_list)
                self.y_list.append(y_list)
                self.z_list.append(z_list)
                
        # set up lines and points
        self.lines = [self.ax.plot([], [], [], linewidth=2)[0] 
                        for _ in range(len(self.uas_paths))]

        self.pts = [self.ax.plot([], [], [], 'o')[0] 
                        for _ in range(len(self.uas_paths))]
        
        for i, (line,pt) in enumerate(zip(self.lines,self.pts)):
            line._color = self.color_list[i]
            pt._color = self.color_list[i]
    
            
        #get which solution is the longest to use as frame reference
        max_list = max(self.uas_paths, key=len)

        self.ani = animation.FuncAnimation(
            self.fig, self.update_multi, frames=len(max_list),repeat=True, 
            interval=5,save_count=len(max_list))
        
        self.ani = animation.FuncAnimation(
            self.fig, self.update_multi, init_func=self.init,
            frames=len(max_list), interval=50, blit=True, 
            repeat=True)
        
        if save == True:
            print("saving")
            # writervideo = FFMpegWriter(fps=10)
            self.ani.save('videos/'+self.method_name+'.mp4', 
                            writer=writervideo)
                    
        plt.show()