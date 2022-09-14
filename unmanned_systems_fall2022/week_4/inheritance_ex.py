"""Heres an example of inheritance"""
class Robot(object):
    def __init__(self, robot_type:str) -> None:
        self.robot_type = robot_type
    
    def turn_on(self) -> None:
        print("I'm turning on ")
    
class Turtlebot(Robot):
    """super refers to what we will be inheriting from, so it will inherit actuator types of robot"""
    def __init__(self, actuator_type:str, lidar_type:str) -> None:
        super().__init__(actuator_type)
        self.lidar_type = lidar_type
        
    def map_area(self) -> None:
        print("I'm mapping area")
    
if __name__ == "__main__":
    turtlebot = Turtlebot("grounded", "360")
    print("turtlebot lidar type", turtlebot.lidar_type)
    print("turtlebot robot_type", turtlebot.robot_type)
    turtlebot.turn_on()
    turtlebot.map_area()
    
    uav = Robot("airvehicle")
    uav.turn_on()
    
        
    
        