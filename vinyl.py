from physical_media import PhysicalMedia
from datetime import date
from decimal import Decimal

class Vinyl(PhysicalMedia):
    def __init__(self, artist, album, release_year, genre, label, country, purchase_date, purchase_price, notes, current_market_value, location, catalog_number, color, edition, condition, record_size, speed, format):
        super().__init__(artist, album, release_year, genre, label, country, purchase_date, purchase_price, notes, current_market_value, location, catalog_number, color, edition, condition)
        self.record_size = record_size
        self.speed = speed
        self.format = format

