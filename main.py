from datetime import date
from decimal import Decimal
from vinyl import Vinyl
from music_collection import MusicCollection

record1 = Vinyl("Daft Punk", "Random Access Memories", 2013, "Electronic", "Columbia", "Germany", date(2026, 8, 14), Decimal("29.99"), "Bought new", Decimal("35.00"), "Shelf 1", "88883716861", "Black", "Original Pressing", "Near Mint", 12, 33, "LP")

record2 = Vinyl("Sezen Aksu", "Sen Aglama", 1984, "Pop", "Sembol", "Turkey", date(2025, 8, 15), Decimal("24.99"), "Bought used", Decimal("40.00"), "Very Good Plus", "Shelf 2", "SEMBOL-001", "Black", "Original Pressing", 12, 33, "LP")

collection = MusicCollection()
collection.add_item(record1)
collection.add_item(record2)

collection.show_items()
print("\nSearch result:")
results = collection.find_by_artist("Michael Jackson")
if results:
    for item in results:
        print(item)
else:
    print("Artist not found.")