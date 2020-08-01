from django.urls import path
from sells.views import CartSinglePage, OrderList, AjaxCartForm, AjaxCartList, AjaxCartDetail, AjaxMyCart, ApiMyCart

urlpatterns = [
    path('', OrderList.as_view(), name='order-list'),

    path('rest/', CartSinglePage.as_view(), name='user-carts-rest'),
    path('rest/ajax_get_cart_form', AjaxCartForm.as_view(), name='cart-rest-form'),
    path('rest/ajax_get_cart_list', AjaxCartList.as_view(), name='cart-rest-list'),
    path('rest/ajax_get_cart_detail', AjaxCartDetail.as_view(), name='cart-rest-detail'),
]
