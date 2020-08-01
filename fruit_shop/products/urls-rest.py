from django.urls import path

from products.views import ApiFruit

urlpatterns = [
    path('', ApiFruit.as_view(), name='fruit-api'),
    # path('api/products/', RestApiFruit.as_view(), name='fruit-api-list'),
]

