import django_filters
from django_filters import CharFilter
from .models import Hall

class HallFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    address = CharFilter(field_name='address', lookup_expr='icontains')

    class Meta:
        model = Hall
        fields = '__all__'
        exclude = ['img', 'name', 'address', 'email', 'contactNumber']
