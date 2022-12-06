import random


class Adventurer:
    """This class creates an Adventurer that will traverse the dungeon."""

    def __init__(self, name):
        # randomly generate the adventurer's health
        health = random.randint(75, 100)

        self._name = name
        self._health = {
            "current": health,
            "max": health
        }
        self._potions = {
            "healing": 2,
            "vision": 2,
        }
        self._pillars = {
            "abstraction": 0,
            "encapsulation": 0,
            "inheritance": 0,
            "polymorphism": 0,
        }

    def update_health(self, strength, is_damage=False):
        """This method updates the current HP of the Adventurer."""
        if is_damage:
            self._health['current'] -= strength
        else:
            self._health['current'] += strength

    def __str__(self):
        """This method returns a string representation of the Adventurer."""
        return self._name

    def use_potion(self, potion_type):
        if potion_type == "healing":
            self._potions['healing'] -= 1
        elif potion_type == "vision":
            self._potions['vision'] -= 1
        else:
            raise Exception("Invalid potion type")


# test
player = Adventurer("Mel")
print(player)
