from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.artist} - {self.title}"


class Release(models.Model):
    MEDIA_TYPES = [
        ("vinyl", "Vinyl"),
        ("cd", "CD"),
        ("cassette", "Cassette"),
        ("digital", "Digital"),
    ]

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="releases"
    )

    media_type = models.CharField(
        max_length=20,
        choices=MEDIA_TYPES
    )

    label = models.CharField(max_length=200, blank=True)
    catalog_number = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    edition = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.album} ({self.get_media_type_display()})"



class CollectionItem(models.Model):
    release = models.ForeignKey(
        Release,
        on_delete=models.CASCADE,
        related_name="collection_items"
    )

    purchase_date = models.DateField(
        null=True,
        blank=True
    )

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    condition = models.CharField(
        max_length=50,
        blank=True
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    current_market_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.release} - Copy #{self.pk}"


