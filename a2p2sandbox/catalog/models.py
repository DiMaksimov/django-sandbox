from django.db import models
from django.utils import timezone

IMAGES_PATH = 'images/catalog/'


# Create your models here.
class CatalogItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated_timestamp = models.DateTimeField(auto_now=True, verbose_name='Updated')
    item_image = models.ImageField(default=f'{IMAGES_PATH}default.jpg', upload_to=f'{IMAGES_PATH}items_images/')

    def __str__(self):
        return self.title
