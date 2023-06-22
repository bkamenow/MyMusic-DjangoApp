from django.db import models

from custom_validators.validators import validate_positive_number


# Create your models here.


class AlbumModel(models.Model):
    GENRE_CHOICES = [
        ('pop', 'Pop Music'),
        ('jazz', 'Jazz Music'),
        ('rnb', 'R&B Music'),
        ('rock', 'Rock Music'),
        ('country', 'Country Music'),
        ('dance', 'Dance Music'),
        ('hiphop', 'Hip Hop Music'),
        ('other', 'Other'),
    ]
    album_name = models.CharField(blank=False, null=False, unique=True, max_length=30)
    artist = models.CharField(blank=False, null=False, max_length=30)
    genre = models.CharField(blank=False, null=False, max_length=30, choices=GENRE_CHOICES)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False, validators=[validate_positive_number])
