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
        self.song_4 = Song("The Wizard", "Black Sabbath")

        # default guests for room_1
        self.guest_1 = Guest("Bob", self.song_1, self.song_1)
        self.guest_2 = Guest("Rob", self.song_2, self.song_2, wallet=5)

        # additional guests for room_1
        self.guest_3 = Guest("Ben", self.song_2, self.song_2)
        self.guest_4 = Guest("George", self.song_1, self.song_1, wallet=20)
        self.guest_5 = Guest("Amy", self.song_2, self.song_2)
        self.guest_6 = Guest("Hilda", self.song_3, self.song_3)
        self.guest_7 = Guest("Ally", self.song_2, self.song_1)
        self.guest_8 = Guest("Mike", self.song_3, self.song_3)
        self.guest_9 = Guest("Janice", self.song_2, self.song_2)
        self.guest_10 = Guest("Clive", self.song_1, self.song_1)
        self.guest_11 = Guest("Skint Dave", self.song_1, self.song_4, wallet=1)


        # default lists for room_1
        self.song_list = [self.song_1, self.song_2]
        self.room_1_guests = [self.guest_1, self.guest_2]
        self.room_1 = Room(self.room_1_guests, self.song_list)
        self.room_2 = Room(self.room_1_guests, [self.song_3, self.song_4])
    
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
        
    def test_check_number_of_guests(self):
        self.room_1.add_multiple_guests(self.guest_3, self.guest_4)
        self.assertEqual(4, self.room_1.check_number_of_guests())

    def test_add_multiple_guests(self):
        self.room_1.add_multiple_guests(self.guest_3, self.guest_4, self.guest_5, self.guest_6,
                                        self.guest_7)
        self.assertEqual(self.room_1.guest_list, [self.guest_1, self.guest_2, self.guest_3, self.guest_4, self.guest_5, self.guest_6,
                                        self.guest_7])

    def test_add_multiple_guests_too_many(self):
        self.room_1.add_multiple_guests(self.guest_3, self.guest_4, self.guest_5, self.guest_6,
                                        self.guest_7, self.guest_8, self.guest_9, self.guest_10)
        self.assertEqual(self.room_1.guest_list, [self.guest_1, self.guest_2, self.guest_3, self.guest_4, self.guest_5, self.guest_6,
                                        self.guest_7, self.guest_8, self.guest_9])

    def test_add_single_guests_too_many(self):
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_in_guest(self.guest_4)
        self.room_1.check_in_guest(self.guest_5)
        self.room_1.check_in_guest(self.guest_6)
        self.room_1.check_in_guest(self.guest_7)
        self.room_1.check_in_guest(self.guest_8)
        self.room_1.check_in_guest(self.guest_9)
        self.room_1.check_in_guest(self.guest_10)

        self.assertEqual(self.room_1.guest_list, [self.guest_1, self.guest_2, self.guest_3, self.guest_4, self.guest_5, self.guest_6,
                                        self.guest_7, self.guest_8, self.guest_9])
        
    def test_check_entry_price(self):
        self.assertEqual(5, self.room_1.entry)

    def test_customer_has_enough_money_enough(self):
        self.assertEqual(True, self.room_1.guest_has_enough_money(self.guest_1))

    def test_customer_has_enough_money_equal(self):
        self.assertEqual(True, self.room_1.guest_has_enough_money(self.guest_2))

    def test_customer_has_enough_money_not_enough(self):
        self.assertEqual(False, self.room_1.guest_has_enough_money(self.guest_11))

    def test_add_customer_to_guest_list_if_can_afford(self):
        self.room_1.check_in_guest(self.guest_11)
        self.assertEqual(self.room_1.guest_list, [self.guest_1, self.guest_2])

    def test_room_has_guests_favourite_song__not_available(self):
        has_song = self.room_1.room_has_guests_favourite_song(self.guest_11)
        self.assertEqual(None, has_song)

    def test_room_has_guests_favourite_song_available(self):
        has_song = self.room_2.room_has_guests_favourite_song(self.guest_11)
        self.assertEqual("Skint Dave screams 'Whoo! yeah!!'", has_song)

    def test_add_to_total_entry_fees(self):
        self.room_1.check_in_guest(self.guest_5)
        self.assertEqual(15, self.room_1.total_entry_fees)

    def test_add_to_total_entry_fees_if_too_many_guests(self):
        self.test_add_multiple_guests_too_many()
        self.assertEqual(45, self.room_1.total_entry_fees)
    

    