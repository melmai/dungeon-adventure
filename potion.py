import random


class HealingPotion:
    """This class creates a Healing Potion instance 
    with a randomly assigned strength between 5 and 15."""
    def __init__(self):
        self._strength = random.randint(5, 15)

    @property
    def strength(self):
        return self._strength

    def __str__(self):
        return f"+{self.strength}HP"
