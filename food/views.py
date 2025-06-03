from rest_framework import viewsets
from .models import Restaurant, MenuItem
from rest_framework import permissions
from .serializers import RestaurantSerializer, MenuItemSerializer
from django_filters.rest_framework import DjangoFilterBackend


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['restaurant'] 