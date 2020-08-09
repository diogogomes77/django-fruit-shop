from django.urls import path

from products.views import ApiFruit

urlpatterns = [
    path('', ApiFruit.as_view(), name='fruit-api'),
    path('<int:id>/', ApiFruit.as_view(), name='fruit-api-detail'),
]


