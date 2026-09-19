from music_item import MusicItem

class DigitalMedia(MusicItem):
    def __init__(self, artist, album, release_year, genre, label, country, purchase_date, purchase_price, notes, current_market_value, file_format):
        super().__init__(artist, album, release_year, genre, label, country, purchase_date, purchase_price, notes, current_market_value)
        self.file_format = file_format