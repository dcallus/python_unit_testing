import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class RoomTest(unittest.TestCase):

    def setUp(self):
        
        self.song_1 = Song("Ring of Fire", "Johnny Cash")
        self.song_2 = Song("Common People", "Pulp")
        self.guest_1 = Guest("Bob", self.song_1)
        self.guest_2 = Guest("Rob", self.song_2)
        self.guest_3 = Guest("Ben", self.song_2)

        self.room_1_guests = [self.guest_1, self.guest_2]
        self.song_list = [self.song_1, self.song_2]

        self.room_1 = Room(self.room_1_guests, self.song_list)
    
    def test_room_has_guest_list(self):
        self.assertEqual(self.room_1.guest_list, self.room_1_guests)

    def test_room_has_song_list(self):
        self.assertEqual(self.room_1.song_list, self.song_list)
    
    def test_room_add_guest_to_list(self):
        self.room_1.check_in_guest(self.guest_3)
        self.assertEqual(self.room_1.guest_list, [self.guest_1, self.guest_2, self.guest_3])