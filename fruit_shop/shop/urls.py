from django.urls import path
from shop.views import ShopSinglePage

urlpatterns = [
    path('', ShopSinglePage.as_view(), name='home'),
]
