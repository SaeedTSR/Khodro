from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Khodro
from .serializers import KhodroSerializer
from .filters import KhodroFilter
from .pagination import DefaultPagination

class KhodroViewSet(ModelViewSet):
    queryset = Khodro.objects.all()
    serializer_class = KhodroSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = KhodroFilter
    pagination_class = DefaultPagination
    search_fields = ['owner_name']
    ordering_fields = ['created_date']