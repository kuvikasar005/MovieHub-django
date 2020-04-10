from django.db import models
from movie.models import Movie
from hall.models import Hall

# Create your models here.
class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    showDate = models.DateField(auto_now_add=False, auto_now=False)
    startTime = models.TimeField( auto_now_add=False, auto_now=False)
    endTime = models.TimeField( auto_now_add=False, auto_now=False)
    seats = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        title = self.movie.name + ' / ' + self.hall.name + ' / ' + str(self.showDate) + ' / ' + str(self.startTime)
        return title
