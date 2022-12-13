import random

class Pit:
    def __init__(self):
        self._damage = random.randint(1, 20)

    @property
    def damage(self):
        """Returns the damage to inflict on the player."""
        return self._damage
