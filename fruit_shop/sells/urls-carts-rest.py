from django.urls import path, include
from sells.views import ApiCart, ApiCartItems, ApiMyCart

urlpatterns = [
    path('', ApiCart.as_view(), name='cart-api-list'),
    path('mycart/', ApiMyCart.as_view(), name='mycart'),
    path('<int>/', ApiCart.as_view(), name='cart-api-details'),
    path('<int:id>/items/', include([
        path('', ApiCartItems.as_view(), name='cart-api-items-list'),
        path('<int:item_id>/', ApiCartItems.as_view(), name='cart-api-items-details'),
    ])),
]
