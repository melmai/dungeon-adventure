from adventurer import Adventurer
from dungeon import Dungeon


class DungeonAdventure:
    def __init__(self):
        self._player = ""
        self._dungeon = None
        self._difficulty = 0
        self._active_room = None

    @property
    def player(self):
        """Returns the Adventurer and prints out its status"""
        return self._player

    @property
    def dungeon(self):
        """Returns the generated dungeon"""
        return self._dungeon

    @property
    def active_room(self):
        """Returns the player's current room"""
        return self._active_room

    @active_room.setter
    def active_room(self, room):
        self._active_room = room

    def print_intro(self):
        """Prints game instructions for player"""
        intro = """
        This is an adventure game where a hero is randomly placed 
        within a dungeon, which is randomly generated. The adventurer 
        needs to find the four Pillars of OO (Abstraction, Encapsulation, 
        Inheritance, and Polymorphism) and take them to the exit to win 
        the game. Some features of the dungeon will prove a hindrance to 
        the adventurer's task (pits), while some will prove helpful. For 
        menu options at any time press m (healing and vision potions).

        Game starting...
        """

        print(intro)

    def play_game(self):
        """Enters player into game loop"""
        command = input("Enter a direction or use item:\n")
        if self.is_move_valid(command):
            self.move(command)
            print(self._active_room)
        else:
            print("The way is blocked!")

    def create_player(self):
        """Gets name for player and creates instance of Adventurer"""
        name = input("What shall we call you, oh brave adventurer?\n")
        self._player = Adventurer(name)

    def create_dungeon(self):
        """Creates dungeon based on player input"""
        size = 0

        while size == 0:
            # get user input
            difficulty = input("Choose your difficulty level (1 - Easy, 2 - Medium, 3 - Hard)\n")

            # set difficulty and dungeon size
            if difficulty == "1":
                size = 5
            elif difficulty == "2":
                size = 7
            elif difficulty == "3":
                size = 10
            else:
                print("Hmm, that's not an option...\n")

        # create/set dungeon and difficulty
        dungeon = Dungeon(size, size)
        dungeon.generate()
        dungeon.fill_rooms()
        self._dungeon = dungeon
        self._difficulty = int(difficulty)

        # set active room to entrance
        self._active_room = dungeon.get_room(dungeon.entrance_row, dungeon.entrance_col)


    def print_game_options(self):
        """Provides movement and action keys for the player"""
        output = """
        Movement:
        n = north, s = south, e = east, w = west
        x = exit (requires all 4 pillars)

        Use Inventory Items:
        h = healing potion, v = vision potion
        """

        print(output)

    def is_move_valid(self, direction):
        if direction == "n":
            return self._active_room.north
        if direction == "s":
            return self._active_room.south
        if direction == "e":
            return self._active_room.east
        if direction == "w":
            return self._active_room.west
        else:
            raise Exception("That's not a valid direction!")



    def move(self, direction):
        directions = {"n": (0, -1), "s": (0, 1), "e": (1, 0), "w": (-1, 0)}
        movement = directions.get(direction)
        self._active_room = self._dungeon.get_room(
            self._active_room.row + movement[0],
            self._active_room.col + movement[1]
        )


if __name__ == '__main__':
    game = DungeonAdventure()
    game.print_intro()
    game.create_player()
    print(game.player)
    game.create_dungeon()
    game.dungeon.draw()
    game.print_game_options()
    print(game.active_room)
    game.play_game()