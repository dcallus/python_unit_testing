class Room:
    def __init__(self, guest_list: list, song_list: list, max_guests=9):
        self.guest_list = guest_list
        self.song_list = song_list

    def check_in_guest(self, guest):
        self.guest_list.append(guest)

    def remove_guest(self, guest):
        self.guest_list.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def remove_song(self, song):
        self.song_list.remove(song)

    def add_multiple_guests(self, *guests):
        for guest in guests: 
            self.guest_list.append(guest)
        print(self.guest_list)