from django.urls import reverse_lazy
from django.views import generic

from products.models import FruitCategory
from products.views.views_utils import StaffOnly


class FruitCategoryList(generic.ListView):
    model = FruitCategory
    fields = '__all__'


class FruitCategoryCreate(StaffOnly, generic.CreateView):
    model = FruitCategory
    fields = '__all__'
    success_url = reverse_lazy('fruit_category-list')


class FruitCategoryUpdate(StaffOnly, generic.UpdateView):
    model = FruitCategory
    fields = '__all__'
    success_url = reverse_lazy('fruit_category-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(str(context))
        return context


class FruitCategoryDelete(StaffOnly, generic.DeleteView):
    model = FruitCategory
    success_url = reverse_lazy('fruit_category-list')
