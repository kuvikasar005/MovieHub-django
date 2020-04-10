import django_filters
from django_filters import CharFilter
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    desc = CharFilter(field_name='desc', lookup_expr='icontains')
    cast = CharFilter(field_name='cast', lookup_expr='icontains')

    class Meta:
        model = Movie
        field = '__all__'
        exclude = ['img', 'thumbnail_img', 'trailer', 'name', 'cast', 'trailer']
