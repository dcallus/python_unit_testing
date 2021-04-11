import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class RoomTest(unittest.TestCase):

    def setUp(self):
        
        #default songs for room_1
        self.song_1 = Song("Ring of Fire", "Johnny Cash")
        self.song_2 = Song("Song 2", "Blur")

        # additional songs
        self.song_3 = Song("Common People", "Pulp")

        # default guests for room_1
        self.guest_1 = Guest("Bob", self.song_1)
        self.guest_2 = Guest("Rob", self.song_2)

        # additional guests for room_1
        self.guest_3 = Guest("Ben", self.song_2)
        self.guest_4 = Guest("George", self.song_1)
        self.guest_5 = Guest("Amy", self.song_2)
        self.guest_6 = Guest("Hilda", self.song_3)
        self.guest_7 = Guest("Ally", self.song_2)
        self.guest_8 = Guest("Mike", self.song_3)
        self.guest_9 = Guest("Janice", self.song_2)
        self.guest_10 = Guest("Clive", self.song_1)


        # default lists for room_1
        self.song_list = [self.song_1, self.song_2]
        self.room_1_guests = [self.guest_1, self.guest_2]
        self.room_1 = Room(self.room_1_guests, self.song_list)
    
    def test_room_has_guest_list(self):
        self.assertEqual(self.room_1.guest_list, self.room_1_guests)

    def test_room_has_song_list(self):
        self.assertEqual(self.room_1.song_list, self.song_list)
    
    def test_room_add_guest_to_list(self):
        self.room_1.check_in_guest(self.guest_3)
        self.assertEqual(self.room_1.guest_list, [self.guest_1, self.guest_2, self.guest_3])

    def test_room_remove_guest_from_list(self):
        self.room_1.remove_guest(self.guest_1)
        self.assertEqual(self.room_1.guest_list, [self.guest_2])

    def test_add_song_to_song_list(self):
        self.room_1.add_song(self.song_3)
        self.assertEqual(self.room_1.song_list, [self.song_1, self.song_2, self.song_3])

    def test_remove_song_from_song_list(self):
        self.room_1.remove_song(self.song_1)
        self.assertEqual(self.room_1.song_list, [self.song_2])

    def test_add_multiple_guests(self):
        self.room_1.add_multiple_guests(self.guest_3, self.guest_4, self.guest_5, self.guest_6,
                                        self.guest_7, self.guest_8, self.guest_9, self.guest_10)

        self.assertEqual(self.room_1.guest_list, [self.guest_1, self.guest_2, self.guest_3, self.guest_4, self.guest_5, self.guest_6,
                                        self.guest_7, self.guest_8, self.guest_9, self.guest_10])

        