from adventurer import Adventurer
from dungeon import Dungeon
from potion import HealingPotion
import textwrap


class DungeonAdventure:
    def __init__(self):
        self._player = None
        self._dungeon = None
        self._difficulty = 0
        self._active_room = None
        self._game_over = False
        self._can_exit = False
        self._found_exit = False
        self.print_intro()
        self.start_game()

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

    @staticmethod
    def print_intro():
        """Prints game instructions for player"""
        intro = """
        This is an adventure game where a hero is randomly placed 
        within a dungeon, which is randomly generated. Your goal is to 
        find the four Pillars of OO (Abstraction, Encapsulation, 
        Inheritance, and Polymorphism) and take them to the exit to win 
        the game. Some features of the dungeon will prove a hindrance to 
        the adventurer's task (pits), while some will prove helpful (potions). 
        
        For menu options at any time press (o).

        Game starting...
        """

        print(textwrap.dedent(intro))

    def play_game(self):
        """Enters player into game loop"""
        while not self._game_over:
            command = input("What do you want to do? (o) see actions / (q) "
                            "quit:\n\n")

            # run command if input is valid
            if self.is_valid(command):
                self.execute_command(command)
            else:
                print("Sorry, that doesn't make sense.")

        self.end_game(self.check_win())

    def execute_command(self, command):
        """
        Runs player command
        :param command: keyboard input from player
        :return: None
        """
        if command == "q":  # quit
            self._game_over = True
        elif command == "x":  # exit
            self.check_win(False)
        elif command == "h":  # use healing potion
            self.player.use_healing_potion()
        elif command == "v":  # use vision potion
            potion_removed = self.player.use_vision_potion()  #
            # true if potion used, false otherwise
            if potion_removed:
                self._dungeon.vision_potion(self.active_room.row,
                                            self.active_room.col)
                print()
        elif command == "i":  # check status and inventory
            print(self.player)
            print(self.active_room)
            print()
        elif command == "o":  # check action options
            self.print_game_options()
        elif command == "m":  # view map
            self.dungeon.draw()
            print("\nHey now, no peeking!")
        elif command == "r":
            print(self.active_room)
            print()
        else:  # otherwise player wants to move
            self.move(command)

    @staticmethod
    def is_valid(command):
        """
        Checks to see if the player's input is a valid command
        :param command: keyboard input from player
        :return: Boolean
        """
        return command in ["w", "a", "s", "d", "x", "v", "h", "q", "i", "o",
                           "m", "r"]

    def check_win(self, is_quitting=True):
        """
        Checks to see if the player has all pillars while in the exit room
        and triggers game end if True
        :return: Boolean
        """
        # check win conditions
        has_won = self.active_room is not None \
            and self.active_room.is_exit() \
            and self.player.mission_complete()

        if not is_quitting:
            # if won, end the game
            if has_won:
                self._game_over = True
            # otherwise tell the player what they're missing
            elif not self.active_room.is_exit():
                print("This isn't the exit...")
            else:  # need more pillars
                print("I'm afraid you're missing some pillars, "
                      "friend. Check your inventory.")

        return has_won

    def start_game(self):
        """
        Sets up new player, dungeon and runs game loop
        :return: None
        """
        self.create_player()
        self.create_dungeon()
        self.play_game()

    def end_game(self, win):
        """
        Congratulates the player if winning conditions are met and offers to
        restart the game
        :param win: True if win conditions met
        :return: None
        """
        # tell the player they've won if applicable
        if win:
            print("You did it!")
            print(self.player)
            print()
            self._dungeon.draw()

        # always ask to restart
        try_again = input("Care to try again? (y/n)\n")
        if try_again == "y":
            print("OK let's try it again! Creating a new dungeon...\n")
            self._game_over = False
            self.start_game()
        elif try_again == "n":
            print("OK, come back and try again!")
        else:
            print("Sorry, I didn't catch that...\n")
            self.end_game(False)

    def create_player(self):
        """Gets name for player and creates instance of Adventurer"""
        name = input("What shall we call you, oh brave adventurer?\n")
        self._player = Adventurer(name)

    def create_dungeon(self):
        """Creates dungeon based on player input"""
        size = 0
        difficulty = self._difficulty

        while size == 0:
            # get user input
            difficulty = input(
                "Choose your difficulty level (1 - Easy, 2 - Medium, "
                "3 - Hard)\n")

            # set difficulty and dungeon size
            if difficulty == "1":
                size = 3
            elif difficulty == "2":
                size = 5
            elif difficulty == "3":
                size = 7
            else:
                print("Hmm, that's not an option...\n")

        # create/set dungeon and difficulty
        dungeon = Dungeon(size, size)
        dungeon.generate()
        if difficulty == "1":
            dungeon.item_spawn_chance = 0.25
            dungeon.pit_spawn_chance = 0.1
        elif difficulty == "2":
            dungeon.item_spawn_chance = 0.2
            dungeon.pit_spawn_chance = 0.15
        elif difficulty == "3":
            dungeon.item_spawn_chance = 0.15
            dungeon.pit_spawn_chance = 0.2
        dungeon.fill_rooms()
        self._dungeon = dungeon
        self._difficulty = int(difficulty)

        # set active room to entrance
        self._active_room = dungeon.get_room(dungeon.entrance_row,
                                             dungeon.entrance_col)

        # show play options and print current room
        print()
        print(self.active_room)
        print("\nYou wake up in a cold, dark room...")

    @staticmethod
    def print_game_options():
        """Provides movement and action keys for the player"""
        output = """
        Movement:
        w = north, s = south, d = east, a = west
        x = exit (requires all 4 pillars)

        Use Inventory Items:
        h = healing potion, v = vision potion
        
        Actions:
        r = inspect current room
        o = check action options
        i = check status and inventory
        q = quit
        """

        print(textwrap.dedent(output))

    def is_move_valid(self, direction):
        """
        Checks to see if player can move in provided direction
        :param direction: player input corresponding to a direction
        :return: Boolean
        """
        if direction == "w":
            return self._active_room.north
        elif direction == "s":
            return self._active_room.south
        elif direction == "d":
            return self._active_room.east
        else:  # a
            return self._active_room.west

    def move(self, direction):
        """
        Changes the active room of the game
        :param direction: player input corresponding to a direction
        :return: None
        """
        # if there's a door, move rooms
        if self.is_move_valid(direction):
            # stores row/col changes as tuples
            directions = {"w": (-1, 0), "s": (1, 0), "d": (0, 1), "a": (0, -1)}
            movement = directions.get(direction)

            # change rooms
            self._active_room = self._dungeon.get_room(
                self.active_room.row + movement[0],
                self.active_room.col + movement[1]
            )

            # show the player the new room and transfer objects/damage
            print()
            print(self.active_room)
            print()
            self.check_room_inventory()

        # otherwise let player know
        else:
            print(self.active_room)
            print("\nThe way is blocked!")

    def check_room_inventory(self):
        """
        Checks active room to see if it has items and transfers if
        present
        """
        # check if there are potions
        potions = ["healing", "vision"]
        for potion in potions:
            if self.active_room.has_potion(potion):
                print(f"You found a {potion} potion!")
                if potion == "vision":
                    self.player.add_vision_potion()
                else:
                    hp = HealingPotion()
                    self.player.add_healing_potion(hp)
                    print(f"Adding a healing potion of {hp.strength} "
                          f"strength to your inventory.")

                self.active_room.remove_potion(potion)

        # check if there are pits
        if self.active_room.has_pit():
            damage = self.active_room.pit.damage
            print(f"You have fallen into a pit and take {damage} damage.")
            self.player.take_damage(damage)

        # check if there are pillars
        pillars = ["inheritance", "abstraction", "encapsulation",
                   "polymorphism"]
        for pillar in pillars:
            if self.active_room.has_pillar(pillar):
                self.player.add_pillar(pillar)
                self.active_room.remove_pillar(pillar)
                print(f"You found the {pillar} pillar!")

                # this should only run once
                if self.player.mission_complete():
                    print("Congratulations, all pillars have been found!")
                    print("Please head to the exit...")
                    print("...but make sure to watch out for those pits!")

        # check if exit and notify player
        if self.active_room.is_exit() and not self._found_exit:
            print("Congratulations! You've found the exit!")
            print("To exit, you must have all 4 pillars in your possession.")
            self._found_exit = True


if __name__ == '__main__':
    game = DungeonAdventure()
