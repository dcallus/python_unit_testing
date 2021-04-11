class Room:
    def __init__(self, guest_list: list, song_list: list, max_guests=9, entry=5):
        self.guest_list = guest_list
        self.song_list = song_list
        self.max_guests = max_guests
        self.entry = entry
        self.bar_till = 0
        self.total_entry_fees = len(guest_list) * entry

    def check_number_of_guests(self):
        return len(self.guest_list)

    def _add_guest(self, guest):
        if self.check_number_of_guests() < self.max_guests and self.guest_has_enough_money(guest, self.entry): 
                self.guest_list.append(guest)
                guest.take_money_from_wallet(self.entry)
                self.add_to_total_entry_fees()
        else:
            return

    def check_in_guest(self, guest):
        self._add_guest(guest)

    def remove_guest(self, guest):
        self.guest_list.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def remove_song(self, song):
        self.song_list.remove(song)

    def add_multiple_guests(self, *guests: list):
        for guest in guests: 
            self._add_guest(guest)

    def guest_has_enough_money(self, guest, item):
        if guest.wallet >= item:
            return True
        return False

    def room_has_guests_favourite_song(self, guest):
        if guest.favourite_song in self.song_list:
            return f"{guest.name} screams 'Whoo! yeah!!'"
    
    def add_to_total_entry_fees(self):
        self.total_entry_fees += self.entry
    
    def guest_buys_drink(self, guest, drink):
        if self.guest_has_enough_money(guest, drink.price):
            guest.take_money_from_wallet(drink.price)
            self.bar_till += drink.price

    