"""
Why classes?     


Two methods of coding:
1. Procedural 
2. OOP - Object Oriented Programming
   - encapsulation -> define attributes of our object and what methods it can do 
   - abstraction -> we reduce complexity of our system 

When Making a class

Making Djikstras class:
    - attributes:
        start 
        goal 
        bounds 
        collision_list 
        
    - what methods:
        - find_path -> return path 
        - get_neighbors
        - check_collision 

create a moving car:
    car should have wheels 
    car should have position
    car should have method to go 
    car should have method to make it stop
"""

def make_car(car_name:str) -> str:
    return car_name

def make_wheels(wheels: str) -> str:
    return wheels 
    
def define_car_position(position: list) -> list:
    return position
    
def move_car(old_position: list) -> list:
    """move car one unit over"""
    new_position = [old_position[0] + 1, old_position[1] + 1]
    return new_position

class Car(object):
    def __init__(self, name, init_position, wheels) -> None:
        self.car_name = name
        self.position = init_position
        self.wheels = wheels
        
    def move_car(self):
        """move car one unit over"""
        self.position = [self.position[0] + 1, self.position[1] + 1]
    
      
        
if __name__ == "__main__":

    toyota_car = Car("Toyota", [0,0], "Firestone")
    musta_car = Car("Mustang", [1,0], "Michelin")
    
    