import unittest
from dungeon import Dungeon
from room import Room


class DungeonAndRoomTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.dungeon = Dungeon()
        self.room = Room(0, 0)

    def testCreateRoom(self):
        self.assertIsInstance(self.room, Room, "A Room was not created")

    def testCreateDungeon(self):
        self.assertIsInstance(self.dungeon, Dungeon, "A Dungeon was not created")


unittest.main()

