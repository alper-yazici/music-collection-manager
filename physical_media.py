from music_item import MusicItem

class PhysicalMedia(MusicItem):
    def __init__(self, artist, album, release_year, genre, label, country, purchase_date, purchase_price, notes, current_market_value, condition, location, catalog_number, color, edition):
        super().__init__(artist, album, release_year, genre, label, country, purchase_date, purchase_price, notes, current_market_value)
        self.location = location
        self.condition = condition
        self.catalog_number = catalog_number
        self.color = color
        self.edition = edition
        
