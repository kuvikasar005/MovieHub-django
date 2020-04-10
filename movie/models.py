from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    cast = models.TextField()
    trailer = models.CharField(max_length=256)
    img = models.ImageField(upload_to='movie_images')
    thumbnail_img = models.ImageField(upload_to='movie_images')

    def __str__(self):
        return self.name
