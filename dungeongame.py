from room import Room
from dungeon import Dungeon
from adventurer import Adventurer
from potion import HealingPotion

GAME_INSTRUCTIONS = '''
This is an adventure game where a hero is randomly placed within a dungeon,
which is randomly generated. The adventurer needs to find the four Pillars
of OO (Abstraction, Encapsulation, Inheritance, and Polymorphism) and take
them to the exit to win the game. Some features of the dungeon will prove a
hindrance to the adventurer's task (pits), while some will prove helpful. For 
menu options at any time press m.
(healing and vision potions).\n
Game starting...
'''

"""To access full maze display enter 'maze' when prompted to move or use an item"""

MENU = '''
Move - use directions (w,a,s,d)
Healing Potion = h
Vision Potion = v
E - exit
'''

print(GAME_INSTRUCTIONS)
name = input("Enter the name of the adventurer")
dungeon = Dungeon(5, 5)
dungeon.generate()
dungeon.fill_rooms()
adventurer = Adventurer(name, dungeon.get_room(dungeon.entrance_row, dungeon.entrance_col))
while adventurer.health > 0:
    #dungeon.draw()
    print(adventurer)
    print(adventurer._location)
    # on player's turn prompt to move adventurer
    choice = input("Please select a direction to move. Or use an item")

    if choice == "m":
        print(MENU)

    # depending on input will move the adventurer if the way is clear
    if choice == "w" and dungeon.get_room(adventurer._location.row - 1, adventurer._location.col).south is True:
        adventurer.move(dungeon.get_room(adventurer._location.row - 1, adventurer._location.col))
    elif choice == "s" and dungeon.get_room(adventurer._location.row + 1, adventurer._location.col).north is True:
        adventurer.move(dungeon.get_room(adventurer._location.row + 1, adventurer._location.col))
    elif choice == "a" and dungeon.get_room(adventurer._location.row, adventurer._location.col - 1).east is True:
        adventurer.move(dungeon.get_room(adventurer._location.row, adventurer._location.col - 1))
    elif choice == "d" and dungeon.get_room(adventurer._location.row, adventurer._location.col + 1).west is True:
        adventurer.move(dungeon.get_room(adventurer._location.row, adventurer._location.col + 1))
    elif choice != "h" and choice != "v" and choice != "maze" and choice != "E":
        print("The way is blocked or input is not valid.")
    print(adventurer._location)

    # now that the adventurer is in a room check to see if anything happens based on what is in the room
    if dungeon.get_room(adventurer._location.row, adventurer._location.col).pit:
        adventurer_health_before = adventurer._health
        adventurer.take_damage()
        adventurer_health_after = adventurer._health
        print("You took " + str(adventurer_health_before - adventurer_health_after) + " points of damage.")
    if dungeon.get_room(adventurer._location.row, adventurer._location.col).healing_potion:
        adventurer.add_healing_potion()
        dungeon.get_room(adventurer._location.row, adventurer._location.col).healing_potion = False
        print("You picked up a Healing Potion!")
    if dungeon.get_room(adventurer._location.row, adventurer._location.col).vision_potion:
        adventurer.add_vision_potion()
        dungeon.get_room(adventurer._location.row, adventurer._location.col).vision_potion = False
        print("You've picked up a Vision Potion")
    if dungeon.get_room(adventurer._location.row, adventurer._location.col).abstraction:
        adventurer.add_pillar("abstraction")
        dungeon.get_room(adventurer._location.row, adventurer._location.col).abstraction = False
        print("You've found the Abstraction Pillar!")
    if dungeon.get_room(adventurer._location.row, adventurer._location.col).encapsulation:
        adventurer.add_pillar("encapsulation")
        dungeon.get_room(adventurer._location.row, adventurer._location.col).encapsulation = False
        print("You've found the Encapsulation Pillar!")
    if dungeon.get_room(adventurer._location.row, adventurer._location.col).inheritance:
        adventurer.add_pillar("inheritance")
        dungeon.get_room(adventurer._location.row, adventurer._location.col).inheritance = False
        print("You've found the Inheritance Pillar!")
    if dungeon.get_room(adventurer._location.row, adventurer._location.col).polymorphism:
        adventurer.add_pillar("polymorphism")
        dungeon.get_room(adventurer._location.row, adventurer._location.col).polymorphism = False
        print("You've found the Polymorphism Pillar!")

    #player chose to use an item
    if choice == "h":
        print("Using a healing potion")
        adventurer.use_healing_potion()
    if choice == "v":
        print("Using a vision potion!")
        adventurer.use_vision_potion()
        dungeon.vision_potion(adventurer._location.row, adventurer._location.col)

    #ending the game
    if adventurer.mission_complete() == True and \
            dungeon.get_room(adventurer._location.row, adventurer._location.col).exit == True:
        break
    if choice == "E":
        break
    if choice == "maze":
        dungeon.draw()

#Game ending comments
if adventurer.mission_complete():
    print("You won!")
elif choice == "E":
    print("Game ended by player")
else:
    print("You died :(")
dungeon_draw()