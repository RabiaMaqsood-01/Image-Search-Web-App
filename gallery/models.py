
from django.db import models

class Favorite(models.Model):
    image_url = models.URLField()
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.alt_text

