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
        self._vision_potions = 2,
        self._pillars = {
            "abstraction": 0,
            "encapsulation": 0,
            "inheritance": 0,
            "polymorphism": 0,
        }

    @property
    def name(self):
        return self._name

    @property
    def healing_potions(self):
        potion_details = ""
        for healing_potion in self._healing_potions:
            potion_details += str(healing_potion.strength) + "\n"
        return potion_details

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
        details += self.healing_potions
        return details

    def use_vision_potion(self):
        self._vision_potions -= 1

    def use_healing_potion(self):
        print(f"old health: {self._health}")
        if len(self._healing_potions) > 0:
            potion = self._healing_potions.pop()
            self.update_health(potion.strength)
        print(self.healing_potions)
        print(f"new health: {self._health}")
        

# test
player1 = Adventurer("Mel")
print(player1)
player2 = Adventurer("Mel2")
print(player2)

player1.use_healing_potion()
print(player1)
