import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.drink import Drink

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
        self.guest_12 = Guest("Rich Dave", self.song_2, self.song_3, wallet=50)


        # default lists for room_1
        self.song_list = [self.song_1, self.song_2]
        self.room_1_guests = [self.guest_1, self.guest_2]
        self.room_1 = Room(self.room_1_guests, self.song_list)
        self.room_2 = Room(self.room_1_guests, [self.song_3, self.song_4])

        # make drinks
        self.drink_1 = Drink("HopHouse13", 5.50, 5)
        self.drink_2 = Drink("Old Fashioned", 6, 30)
    
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
        self.assertEqual(True, self.room_1.guest_has_enough_money(self.guest_1, self.room_1.entry))

    def test_customer_has_enough_money_equal(self):
        self.assertEqual(True, self.room_1.guest_has_enough_money(self.guest_2,self.room_1.entry))

    def test_customer_has_enough_money_not_enough(self):
        self.assertEqual(False, self.room_1.guest_has_enough_money(self.guest_11, self.room_1.entry))

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

    def test_add_to_total_entry_fees_if_customer_cannot_afford(self):
        self.room_1.check_in_guest(self.guest_11)
        self.assertEqual(10, self.room_1.total_entry_fees)

    def test_take_money_from_customer_after_entry(self):
        self.room_1.check_in_guest(self.guest_4)
        self.assertEqual(15, self.guest_4.wallet)
    
    def test_guest_buys_drink_has_enough_money(self):
        self.room_1.guest_buys_drink(self.guest_1, self.drink_1)
        self.assertEqual(4.5, self.guest_1.wallet)
        self.assertEqual(5.5, self.room_1.bar_till)

    def test_guest_buys_drink_not_enough_money(self):
        self.room_1.guest_buys_drink(self.guest_11, self.drink_1)
        self.assertEqual(1, self.guest_11.wallet)
        self.assertEqual(0, self.room_1.bar_till)
        
    def test_apply_drink_refund(self):
        self.room_1.guest_buys_drink(self.guest_1, self.drink_1)
        self.room_1.apply_drink_refund(self.guest_1, self.drink_1) 
        self.assertEqual(10, self.guest_1.wallet)
        self.assertEqual(0, self.room_1.bar_till)

    def test_guests_removed(self):
        self.room_1.remove_all_guests_from_list()
        self.assertEqual([], self.room_1.guest_list)

    def test_get_total_cash(self):
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_in_guest(self.guest_4)
        self.room_1.check_in_guest(self.guest_5)
        self.room_1.check_in_guest(self.guest_11) # not enough
        self.room_1.guest_buys_drink(self.guest_1, self.drink_1)
  
        self.room_1.guest_buys_drink(self.guest_2, self.drink_1) # not enough
        self.room_1.guest_buys_drink(self.guest_4, self.drink_1)
        self.room_1.guest_buys_drink(self.guest_4, self.drink_1)
        self.room_1.apply_drink_refund(self.guest_1, self.drink_1)
        self.assertEqual(36, self.room_1.get_total_cash())

    def test_add_to_tab__total_current_round(self):
        # guest has enough money, add to dictionary
        self.room_1.add_to_tab(self.guest_12, [self.drink_1, self.drink_2])
        self.assertEqual({self.guest_12:  [self.drink_1, self.drink_2]}, self.room_1.bar_tabs)
        
        # guest doesn't have enough money, do not add to dictionary
        self.room_1.add_to_tab(self.guest_11, [self.drink_1])
        self.assertEqual({self.guest_12:  [self.drink_1, self.drink_2]}, self.room_1.bar_tabs)

        # another guest has enough money, add to dictionary
        self.room_1.add_to_tab(self.guest_4, [self.drink_1, self.drink_1, self.drink_2])
        self.assertEqual({self.guest_12:  [self.drink_1, self.drink_2],
                          self.guest_4:  [self.drink_1, self.drink_1, self.drink_2]
                        }, self.room_1.bar_tabs)

        # guest with tab adds more drinks
        self.room_1.add_to_tab(self.guest_12, [self.drink_1, self.drink_1, self.drink_2])
        self.assertEqual({self.guest_12:  [self.drink_1, self.drink_2, self.drink_1, self.drink_1, self.drink_2],
                          self.guest_4:  [self.drink_1, self.drink_1, self.drink_2]}, self.room_1.bar_tabs)

    def test_money_transferred_from_wallet_to_tab(self):
        self.room_1.add_to_tab(self.guest_12, [self.drink_2, self.drink_2])
        self.assertEqual(12, self.guest_12.tab)

    def test_pay_customer_tab(self):
        self.test_money_transferred_from_wallet_to_tab()
        self.room_1.pay_customer_tab(self.guest_12)
        self.assertEqual(12, self.room_1.bar_till)
