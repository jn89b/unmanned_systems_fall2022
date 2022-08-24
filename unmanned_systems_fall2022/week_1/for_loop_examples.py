# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:20:42 2022

@author: jnguy
"""



#% Import stuff here
import matplotlib.pyplot as plt


#% Classes 
def add(x:float, y:float) -> float:
    return x + y

#% Main 

#%% 
import numpy as np 

x_list = list(np.arange(0,10))
y_list = list(np.arange(10,20))

##basic for loop 
print("og method")
for i in range(0,len(x_list)):
    print("x is ", x_list[i]," " , "y is ", y_list[i])
    
#%%     
##duck typing short hand
print("\n")
print("duck typing")
for x,y in zip(x_list,y_list):
    print("x and y are: ", x,y)
    
    
#%% I need an index counter, as well as go through x and y coordinates
for i, (x,y) in enumerate(zip(x_list,y_list)):
    print("i, x, and y are ", i, x, y )
    
    
#%% How to plot
plt.plot(x_list,y_list)

#%% Testing code
val = add(2,3)
assert val == 10
    