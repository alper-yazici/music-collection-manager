class MusicCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(item)

    def find_by_artist(self, artist):
        results = []
        for item in self.items:
            if item.artist.lower() == artist.lower():
                results.append(item)

        return results

    def find_by_album(self, album):
        results = []
        for item in self.items:
            if item.album.lower() == album.lower():
                results.append(item)

        return results