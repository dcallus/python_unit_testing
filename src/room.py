class Room:
    def __init__(self, guest_list, song_list, max_guests=50):
        self.guest_list = guest_list
        self.song_list = song_list

    def check_in_guest(self, guest):
        self.guest_list.append(guest)