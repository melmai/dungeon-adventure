import random

class Room:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.north = False
        self.south = False
        self.west = False
        self.east = False
        self.healing_potion = False
        self.vision_potion = False
        self.entrance = False
        self.exit = False
        self.pit = False
        self.abstraction = False
        self.encapsulation = False
        self.inheritance = False
        self.polymorphism = False

    def __str__(self):
        result = ""
        self.draw_top()
        print()
        self.draw_middle()
        print()
        self.draw_bottom()
        return result

    def draw_top(self):
        if self.north:
            print("*   *", end="")
        else:
            print("*****", end="")

    def draw_middle(self):
        if self.west:
            print(" ", end="")
        else:
            print("*", end="")
        if self.entrance:
            print(" i ", end="")
        elif self.exit:
            print(" O ", end="")
        elif self.healing_potion:
            if self.vision_potion:
                print(" M ", end="")
            elif self.pit:
                print(" M ", end="")
            elif self.pit == True and self.vision_potion == True:
                print(" M ", end="")
            else:
                print(" H ", end="")
        elif self.vision_potion:
            if self.healing_potion:
                print(" M ", end="")
            elif self.pit:
                print(" M ", end="")
            elif self.pit == True and self.healing_potion == True:
                print(" M ", end="")
            else:
                print(" V ", end="")
        elif self.pit:
            if self.healing_potion:
                print(" M ", end="")
            elif self.vision_potion:
                print(" M ", end="")
            elif self.vision_potion == True and self.healing_potion == True:
                print(" M ", end="")
            else:
                print(" X ", end="")
        elif self.abstraction:
            print(" A ", end="")
        elif self.encapsulation:
            print(" E ", end="")
        elif self.inheritance:
            print(" I ", end="")
        elif self.polymorphism:
            print(" P ", end="")
        else:
            print("   ", end="")
        if self.east:
            print(" ", end="")
        else:
            print("*", end="")

    def draw_bottom(self):
        if self.south:
            print("*   *", end="")
        else:
            print("*****", end="")

    def __repr__(self):
        return str(self)

