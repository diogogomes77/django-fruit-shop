from django.urls import path
from products.api import ApiFruitList

urlpatterns = [
    path('', ApiFruitList.as_view(), name='fruit-api-list'),
    # path('api/products/', RestApiFruit.as_view(), name='fruit-api-list'),
]

