
from django.urls import path
from django.views.generic import TemplateView

from products.views import FruitCategoryCreate, FruitCategoryUpdate, FruitCategoryDelete, FruitCategoryList

urlpatterns = [
    path('', FruitCategoryList.as_view(), name='fruit_category-list'),
    path('add/', FruitCategoryCreate.as_view(), name='fruit_category-add'),
    path('<int:pk>/', FruitCategoryUpdate.as_view(), name='fruit_category-update'),
    path('<int:pk>/delete/', FruitCategoryDelete.as_view(), name='fruit_category-delete'),
]
