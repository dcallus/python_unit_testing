import unittest
from src.song import Song

class SongTest(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Pocket Calculator", "Kraftwerk")
        self.song_2 = Song("Closer to God", "Nine Inch Nails")
        self.song_3 = Song("Cars", "Gary Numan")

    def test_song_title(self):
        self.assertEqual("Pocket Calculator", self.song_1.title)
        
    def test_song_artist(self):
        self.assertEqual("Gary Numan", self.song_3.artist)

    