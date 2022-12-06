from maze import Room
from dungeon import Dungeon

my_map = Dungeon(5, 5)  # assume the rows and columns must be greater than 1
my_map.generate()
my_map.fill_rooms()
#my_map.print()
my_map.draw()

