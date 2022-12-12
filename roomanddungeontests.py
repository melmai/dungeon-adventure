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
    
    def testIsExit(self):
        self.room.exit = True
        self.assertTrue(self.room.is_exit(), "An exit room was not returned")
        
    def testHasPit(self):
        self.room.pit = True
        self.assertTrue(self.room.has_pit(), "A room with a pit was not returned")
    
    def testHasPotion(self):
        self.room.healing_potion = True
        self.assertTrue(self.room.has_potion("healing"), "A room with a healing potion was not returned")
    
    def testHasPillar(self):
        self.room.abstraction = True
        self.assertTrue(self.room.has_pillar("abstraction"), "The room didn't return the abstraction pillar")

    def testCreateDungeon(self):
        self.assertIsInstance(self.dungeon, Dungeon, "A Dungeon was not created")
        
    def testGetRoom(self):
        self.assertIs(self.dungeon.get_room(0,0), self.dungeon.rooms[0][0], "Failed to get the correct room")


unittest.main()
