from django.urls import reverse_lazy
from rest_framework import generics, viewsets

from products.models import Fruit
from products.views.views_utils import StaffOnly


class FruitDrfList(generics.ListAPIView):
    model = Fruit
    fields = '__all__'


class FruitDrfCreate(StaffOnly, generics.CreateAPIView):
    model = Fruit
    fields = '__all__'
    success_url = reverse_lazy('fruit-list')


class FruitDrfUpdate(StaffOnly, generics.UpdateAPIView):
    model = Fruit
    fields = '__all__'
    success_url = reverse_lazy('fruit-list')


class FruitDrfDelete(StaffOnly, generics.DestroyAPIView):
    model = Fruit
    success_url = reverse_lazy('fruit-list')


class FruitDrf(viewsets.ModelViewSet):
    model = Fruit
    fields = '__all__'

