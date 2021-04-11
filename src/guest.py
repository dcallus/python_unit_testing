class Guest:
    def __init__(self, name, song, favourite_song, wallet=10):
        self.name = name
        self.song = song
        self.favourite_song = favourite_song
        self.wallet = wallet

    def take_money_from_wallet(self, amount):
        self.wallet -= amount

    def put_money_in_wallet(self, amount):
        self.wallet += amount