import unittest
import unittest
from src.guest import Guest
from src.song import Song

class GuestTest(unittest.TestCase):
    def setUp(self):

        #set up songs
        self.song_1 = Song("Ring of Fire", "Johnny Cash")
        self.song_2 = Song("Song 2", "Blur")
        
        self.guest_1 = Guest("June", self.song_1)

    def test_guest_name(self):
        self.assertEqual("June", self.guest_1.name)
    
    def test_guest_song(self):
        self.assertEqual(self.song_1, self.guest_1.song)