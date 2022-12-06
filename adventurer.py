import random


class Adventurer:

    def __init__(self, name):
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

    def __str__(self):
        return self._name


# test
player = Adventurer("Mel")
print(player)