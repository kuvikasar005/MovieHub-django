from django.db import models

# Create your models here.
class Offer(models.Model):
    promoCode = models.CharField(max_length=20)
    desc = models.TextField()
    expiryDate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.promoCode
