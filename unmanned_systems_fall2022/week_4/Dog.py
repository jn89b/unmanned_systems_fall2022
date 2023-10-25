from typing import Any


class Dog():
    def __init__(self, name:str) -> None:
        self.name = name
        
    def bark(self):
        print("woof woof bark bark")
        
    def go_chase_bad_guy(self):
        self.bark()
        
        
        
corgi = Dog("apa")

corgi.go_chase_bad_guy()
