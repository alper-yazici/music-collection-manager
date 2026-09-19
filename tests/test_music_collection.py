import unittest
from datetime import date
from decimal import Decimal

from music_collection import MusicCollection
from vinyl import Vinyl

class TestMusicCollectionSearches(unittest.TestCase):
    def setUp(self):
        self.collection = MusicCollection()

        self.record = Vinyl(
            "Daft Punk",
            "Random Access Memories",
            2013,
            "Electronic",
            "Columbia",
            "Germany",
            date(2026, 8, 14),
            Decimal("29.99"),
            "Bought new",
            Decimal("35.00"),
            "Near Mint",
            "Shelf 1",
            "88883716861",
            "Black",
            "Original Pressing",
            12,
            33,
            "LP",
        )

        self.collection.add_item(self.record)


    def test_find_by_artist_returns_matching_item(self):
        results = self.collection.find_by_artist("Daft Punk")

        self.assertEqual(results, [self.record])


    def test_find_by_album_returns_matching_item(self):
        results = self.collection.find_by_album("Random Access Memories")

        self.assertEqual(results, [self.record])


    def test_artist_search_is_case_insensitive(self):
        results = self.collection.find_by_artist("daft punk")

        self.assertEqual(results, [self.record])


    def test_album_search_is_case_insensitive(self):
        results = self.collection.find_by_album("random access memories")

        self.assertEqual(results, [self.record])


    def test_unknown_artist_returns_empty_list(self):
        results = self.collection.find_by_artist("Michael Jackson")

        self.assertEqual(results, [])


    def test_unknown_album_returns_empty_list(self):
        results = self.collection.find_by_album("Thriller")

        self.assertEqual(results, [])