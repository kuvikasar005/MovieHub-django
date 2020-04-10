from django.db import models

# Create your models here.
class Hall(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contactNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
