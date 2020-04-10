from django.db import models
from django.contrib.auth.models import User, auth

from shows.models import Show

# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    show = models.ForeignKey(Show, on_delete=models.SET_NULL, null=True)
    seats = models.IntegerField()
    amount = models.IntegerField()
    method = models.CharField(max_length=100)

    def __str__(self):
        name = str(self.user) + " / " + str(self.show)
        return name
