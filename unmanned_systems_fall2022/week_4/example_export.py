# go to example folder, get hello_world and import 
# add_numbers function
from example.hello_world import add_numbers, \
    subtract_numbers

# from example import hello_world

# z = hello_world.add_numbers(5, 5)
z = add_numbers(5, 5)
subtract_z = subtract_numbers(5,5) 

print(z)
print(subtract_z)

 