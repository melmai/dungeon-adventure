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
    def health(self):
        return self._health

    @health.setter
    def health(self, hp):
        self._health = hp

    @property
    def healing_potions(self):
        potion_details = "Healing Potions: "
        for healing_potion in self._healing_potions:
            potion_details += f"[{str(healing_potion)}]"
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


# test
player1 = Adventurer("Mel")
print(player1)
print()
player2 = Adventurer("Mel2")
print(player2)
print()
player1.use_healing_potion()
print(player1)
