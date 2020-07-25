from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from products.models import Fruit


class FruitList(generic.ListView):
    model = Fruit
    fields = '__all__'


class FruitCreate(generic.CreateView):
    model = Fruit
    fields = '__all__'
    success_url = reverse_lazy('fruit-list')


class FruitUpdate(generic.UpdateView):
    model = Fruit
    fields = '__all__'
    success_url = reverse_lazy('fruit-list')


class FruitDelete(generic.DeleteView):
    model = Fruit
    success_url = reverse_lazy('fruit-list')
