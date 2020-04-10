import django_filters
from django_filters import CharFilter
from .models import Show

class ShowFilter(django_filters.FilterSet):

    class Meta:
        model = Show
        field = '__all__'
        exclude = ['movie', 'showDate', 'startTime', 'endTime', 'seats', 'price']
