from adventurer import Adventurer
from dungeon import Dungeon


class DungeonAdventure:
    def __init__(self):
        self._player = ""
        self._dungeon = None
        self._difficulty = 0

    @property
    def player(self):
        return self._player

    @property
    def dungeon(self):
        return self._dungeon

    def intro(self):
        """Prints game instructions for player"""
        intro = "This is an adventure game where a hero is randomly placed \
            within a dungeon, which is randomly generated. The adventurer \
            needs to find the four Pillars of OO (Abstraction, Encapsulation, \
            Inheritance, and Polymorphism) and take them to the exit to win \
            the game. Some features of the dungeon will prove a hindrance to \
            the adventurer's task (pits), while some will prove helpful. For \
            menu options at any time press m (healing and vision potions).\n \
            Game starting..."

        print(intro)

    def play_game(self):
        pass

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
        self._dungeon = Dungeon(size, size)
        self._difficulty = int(difficulty)



if __name__ == '__main__':
    game = DungeonAdventure()
    game.create_player()
    print(game.player)
    game.create_dungeon()
    print(game.dungeon)

        