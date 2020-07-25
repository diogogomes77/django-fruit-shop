from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from products.models import FruitCategory


class FruitCategoryList(generic.ListView):
    model = FruitCategory
    fields = '__all__'


class FruitCategoryCreate(generic.CreateView):
    model = FruitCategory
    fields = '__all__'
    success_url = reverse_lazy('fruit_category-list')


class FruitCategoryUpdate(generic.UpdateView):
    model = FruitCategory
    fields = '__all__'
    success_url = reverse_lazy('fruit_category-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(str(context))
        return context


class FruitCategoryDelete(generic.DeleteView):
    model = FruitCategory
    success_url = reverse_lazy('fruit_category-list')
