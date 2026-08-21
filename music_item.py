class MusicItem:
    def __init__(self, artist, album, release_year, genre, label, country, purchase_date, purchase_price, notes, current_market_value):
            self.artist = artist
            self.album = album
            self.release_year = release_year
            self.genre = genre
            self.label = label
            self.country = country
            self.purchase_date = purchase_date
            self.purchase_price = purchase_price
            self.notes = notes
            self.current_market_value = current_market_value

    def __str__(self):
          return f"{self.artist} - {self.album}"