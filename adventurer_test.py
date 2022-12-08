from adventurer import Adventurer

# create test players
player1 = Adventurer("Mel")
print(player1)
print()
player2 = Adventurer("Mel2")
print(player2)
print()

# test healing potion use
print("Trying out a health potion!")
player1.use_healing_potion()
print(player1)
print()

# test damage
print("Ouch that hurts.")
player1.take_damage()
print(player1)
print()

# try healing again
print("Ok now lets heal it up")
player1.use_healing_potion()
print(player1)
print()

# simulate finding healing potion
print("YAY found a healing potion!\n")
player1.add_healing_potion()
print(player1)

# mission complete?
print(f"Check to see if all pillars found: {player1.mission_complete()}\n")

# simulate all pillars found
player1.add_pillar("abstraction")
player1.add_pillar("encapsulation")
player1.add_pillar("inheritance")
player1.add_pillar("polymorphism")

# mission complete?
print("OK now we've found them all!\n")
print(player1)
print(f"Check to see if all pillars found: {player1.mission_complete()}")