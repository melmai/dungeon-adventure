from adventurer import Adventurer
from dungeon import Dungeon
from potion import HealingPotion


class DungeonAdventure:
    def __init__(self):
        self._player = ""
        self._dungeon = None
        self._difficulty = 0
        self._active_room = None
        self._game_over = False
        self._can_exit = False
        self._found_exit = False

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
        while not self._game_over:
            command = input("\nEnter a direction or use item:\n")
            print()

            # if input is valid command
            if self.is_valid(command):
                if command == "q": # quit
                    self._game_over = True
                elif command == "x": # exit
                    if self.check_win():
                        self._game_over = True
                elif command == "h": # use healing potion
                    self._player.use_healing_potion()
                elif command == "v": # use vision potion
                    potion_removed = self._player.use_vision_potion() # true if potion used, false otherwise
                    if potion_removed:
                        self._dungeon.vision_potion(self._active_room.row, self._active_room.col)
                else: # otherwise player wants to move

                    # if there's a door, move rooms
                    if self.is_move_valid(command):
                        self.move(command)
                        print(self._active_room)
                        self.check_room_inventory()
                    # otherwise let player know
                    else:
                        print("The way is blocked!")
                        print(self._active_room)
        
            else:
                print("Sorry, that doesn't make sense.")
                self.print_game_options()

        self.end_game(self.check_win())

        
        
    def is_valid(self, command):
        return True if command in ["n", "s", "e", "w", "x", "v", "h", "q"] else False

    
    def check_win(self):
        return self._active_room.is_exit() and self._player.mission_complete()

    def end_game(self, win):
        if win:
            print("You did it!")
            self._dungeon.draw()
        else:
            try_again = input("Try again? (y/n)\n")
            if try_again == "y":
                self.create_dungeon()
                self.play_game()
            elif try_again == "n":
                print("OK, come back and try again!")
            else:
                try_again = input("Sorry, I didn't catch that...\n")
                self.end_game(False)

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
        """Checks to see if player can move in provided direction"""
        if direction == "n":
            return self._active_room.north
        elif direction == "s":
            return self._active_room.south
        elif direction == "e":
            return self._active_room.east
        elif direction == "w":
            return self._active_room.west
        else:
            raise Exception("That's not a valid direction!")

    def move(self, direction):
        """Changes the active room of the game"""
        directions = {"n": (-1,0), "s": (1, 0), "e": (0, 1), "w": (0, -1)}
        movement = directions.get(direction)
        self.active_room = self._dungeon.get_room(
            self.active_room.row + movement[0],
            self.active_room.col + movement[1]
        )

    def check_room_inventory(self):
        """Checks active room to see if it has items and transfers if present"""
        # check if there are potions
        potions = ["healing", "vision"]
        for potion in potions:
            if self._active_room.has_potion(potion):
                print(f"You found a {potion} potion!")
                if potion == "vision":
                    self._player.add_vision_potion()
                else:
                    hp = HealingPotion()
                    self._player.add_healing_potion(hp)
                    print(f"A healing potion of {hp.strength} strength")

                self._active_room.remove_potion(potion)

                # this should only run once
                if self._player.mission_complete():
                    print("Congratulations, all pillars have been found!")
                    print("Please make your way to the exit...")
                    print("...but make sure to watch out for those pits!")

        # check if there are pits
        if self._active_room.has_pit():
            self._player.take_damage()
            print("You have fallen into a pit")

        # check if there are pillars
        pillars = ["inheritance", "abstraction", "encapsulation", "polymorphism"]
        for pillar in pillars:
            if self._active_room.has_pillar(pillar):
                self._player.add_pillar(pillar)
                self._active_room.remove_pillar(pillar)
                print(f"You found a {pillar} potion!")

        # check if exit and notify player
        if self._active_room.is_exit() and not self._found_exit:
            print("Congratulations! You've found the exit!")
            print("To exit, you must have all 4 pillars in your posession.")
            self._found_exit = True


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