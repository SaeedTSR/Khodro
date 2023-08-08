from django_filters.rest_framework import FilterSet
from .models import Khodro

class KhodroFilter(FilterSet):
    class Meta:
        model = Khodro
        fields = {'brand__title':['exact']}