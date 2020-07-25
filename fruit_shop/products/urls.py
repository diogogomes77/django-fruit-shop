
from django.urls import path

from products.views import FruitList, FruitCreate, FruitUpdate, FruitDelete, FruitCategoryList, FruitCategoryCreate, \
    FruitCategoryUpdate, FruitCategoryDelete

urlpatterns = [
    path('', FruitList.as_view(), name='fruit-list'),
    path('add/', FruitCreate.as_view(), name='fruit-add'),
    path('<int:pk>/', FruitUpdate.as_view(), name='fruit-update'),
    path('<int:pk>/delete/', FruitDelete.as_view(), name='fruit-delete'),

    path('/fruit-categories', FruitCategoryList.as_view(), name='fruit_category-list'),
    path('/fruit-categories/add/', FruitCategoryCreate.as_view(), name='fruit_category-add'),
    path('/fruit-categories/<int:pk>/', FruitCategoryUpdate.as_view(), name='fruit_category-update'),
    path('/fruit-categories/<int:pk>/delete/', FruitCategoryDelete.as_view(), name='fruit_category-delete'),
]
