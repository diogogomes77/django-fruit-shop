from django.urls import path

from products.views.views_fruits_drf import FruitDrfList, FruitDrfCreate, FruitDrfUpdate, FruitDrfDelete

urlpatterns = [
    path('', FruitDrfList.as_view(), name='fruit-drf-list'),
    path('add/', FruitDrfCreate.as_view(), name='fruit-drf-add'),
    path('<int:pk>/', FruitDrfUpdate.as_view(), name='fruit-drf-update'),
    path('<int:pk>/delete/', FruitDrfDelete.as_view(), name='fruit-drf-delete'),
]

