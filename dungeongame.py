from room import Room
from dungeon import Dungeon
from adventurer import Adventurer
from potion import HealingPotion

my_map = Dungeon(5, 5)  # assume the rows and columns must be greater than 3, must be enough rooms to fill
my_map.generate()
my_map.fill_rooms()
my_map.draw()
#my_map.get_room(0,0).entrance = True
my_adventurer = Adventurer("Sheehan", my_map.get_room(my_map.entrance_row, my_map.entrance_col)) #creating an Adventurer and setting their location to the entrance
print(my_adventurer._location) #display Adventurer's room
my_adventurer.move(my_map.get_room(my_adventurer._location.row, my_adventurer._location.col + 1)) #example of moving east in the dungeon
print(my_adventurer._location) # new room adventurer moved to
my_map.vision_potion(my_adventurer._location.row, my_adventurer._location.col) # example of vision potion in use
