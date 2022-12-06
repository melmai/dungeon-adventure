import random
from potion import HealingPotion


class Adventurer:
    """This class creates an Adventurer that will traverse the dungeon."""

    def __init__(self, name):
        # randomly generate the adventurer's health
        health = random.randint(75, 100)

        self._name = name
        self._health = self._health_max = health
        self._healing_potions = [
            HealingPotion(),
            HealingPotion()
        ]
        self._vision_potions = 2
        self._pillars = {
            "abstraction": False,
            "encapsulation": False,
            "inheritance": False,
            "polymorphism": False,
        }

    @property
    def name(self):
        """This method returns the Adventurer's name."""
        return self._name

    @property
    def health(self):
        """This method gets the current HP value of the Adventurer."""
        return self._health

    @health.setter
    def health(self, hp):
        """This method sets the HP value of the Adventurer."""
        self._health = hp

    @property
    def healing_potions(self):
        """This method gets the current healing potions in the inventory."""
        potion_details = "Healing Potions: "
        for healing_potion in self._healing_potions:
            potion_details += f"[{str(healing_potion)}]"
        return potion_details

    @property
    def pillars(self):
        """This method gets the current pillars in the inventory."""
        pillars = "Pillars: "
        for pillar, status in self._pillars.items():
            result = 1 if status else 0
            pillars += f"{pillar.capitalize()}: {result}/1\n"
        return pillars    
        
    def update_health(self, strength, is_damage=False):
        """This method updates the current HP of the Adventurer."""
        if is_damage:
            self._health -= strength
        else:
            self._health += strength

    def __str__(self):
        """This method returns a string representation of the Adventurer."""
        details = ""
        details += self._name + "\n"
        details += f"{self.health}/{self._health_max}\n\n"
        details += self.healing_potions + "\n"
        details += f"Vision Potions: {self._vision_potions}\n\n"
        details += self.pillars
        return details

    def add_vision_potion(self):
        """This method increments inventory value of Vision Potions"""
        self._vision_potions += 1

    def use_vision_potion(self):
        """This method decrements inventory value of Vision Potions"""
        if self._vision_potions > 0:
            self._vision_potions -= 1
            return True
        else: 
            print("Sorry, no vision potions available!")
            return False

    def add_healing_potion(self):
        """This method adds a Healing Potion object to the inventory."""
        self._healing_potions.append(HealingPotion())

    def use_healing_potion(self):
        """This method updates the HP of the Adventurer, up to max HP."""

        # don't use a potion if already at full strength
        if self.health >= self._health_max:
            print("Already at full strength!")
            return

        # check to see that there are potions available
        if len(self._healing_potions) > 0:
            potion = self._healing_potions.pop()
            self.update_health(potion.strength)

            # make sure current HP does not exceed max HP
            if self.health > self._health_max: 
                self.health = self._health_max

        # if not, let the user know
        else:
            print("Sorry, no health potions available!")

    def add_pillar(self, pillar):
        """This method adds a pillar to the inventory."""
        if pillar == "abstraction":
            self._pillars["abstraction"] = True
        elif pillar == "encapsulation":
            self._pillars["encapsulation"] = True
        elif pillar == "inheritance":
            self._pillars["inheritance"] = True
        elif pillar == "polymorphism":
            self._pillars["polymorphism"] = True
        else:
            raise Exception("That's not a pillar...")
    
    def mission_complete(self):
        return self._pillars["abstraction"] and self._pillars["encapsulation"] \
            and self._pillars["inheritance"] and self._pillars["polymorphism"]

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
player1.update_health(10, True)
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