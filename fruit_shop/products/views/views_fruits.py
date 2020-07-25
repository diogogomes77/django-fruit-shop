from django.urls import reverse_lazy
from django.views import generic

from products.models import Fruit
from products.views.views_utils import StaffOnly


class FruitList(generic.ListView):
    model = Fruit
    fields = '__all__'


class FruitCreate(StaffOnly, generic.CreateView):
    model = Fruit
    fields = '__all__'
    success_url = reverse_lazy('fruit-list')


class FruitUpdate(StaffOnly, generic.UpdateView):
    model = Fruit
    fields = '__all__'
    success_url = reverse_lazy('fruit-list')


class FruitDelete(StaffOnly, generic.DeleteView):
    model = Fruit
    success_url = reverse_lazy('fruit-list')
