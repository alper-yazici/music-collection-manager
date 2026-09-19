from physical_media import PhysicalMedia

class Vinyl(PhysicalMedia):
    def __init__(self, artist, album, release_year, genre, label, country, purchase_date, purchase_price, notes, current_market_value, condition, location, catalog_number, color, edition, record_size, speed, format):
        super().__init__(artist, album, release_year, genre, label, country, purchase_date, purchase_price, notes, current_market_value, condition, location, catalog_number, color, edition)
        self.record_size = record_size
        self.speed = speed
        self.format = format

