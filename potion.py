import random


class HealingPotion:
    """This class creates a Healing Potion instance 
    with a randomly assigned strength between 5 and 15."""
    def __init__(self):
        self._strength = random.randint(5, 15)

    @property
    def strength(self):
        """Returns the amount of healing strength of the Potion instance."""
        return self._strength

    def __str__(self):
        """Returns a string representation of the strength of the Potion."""
        return f"+{self.strength}HP"
