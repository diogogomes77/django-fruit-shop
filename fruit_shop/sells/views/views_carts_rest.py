import json

from django.contrib.auth.models import AnonymousUser
from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import BaseDeleteView, DeletionMixin

from products.models import Fruit
from sells.models import ShoppingCart, CartItem
from users.models import ShopUser


class ApiCartList(generic.ListView):

    def get(self, request, *args, **kwargs):
        carts = ShoppingCart.objects.all().values('user', 'items')
        data = list(carts)
        return JsonResponse(data, safe=False)


class ApiCartDetail(generic.DetailView):
    model = ShoppingCart
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        cart = ShoppingCart.objects.get(pk=kwargs['id'])
        data = model_to_dict(cart)
        return JsonResponse(data, safe=False)


class ApiCartCreate(generic.CreateView):
    model = ShoppingCart
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        print('post')
        self.object = None
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        print('get_success_url')
        return reverse_lazy('Cart-api')


class ApiCart(View):

    def get(self, request, *args, **kwargs):

        if len(kwargs) > 0:
            view = ApiCartDetail.as_view()
        else:
            view = ApiCartList.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        view = ApiCartCreate.as_view()
        return view(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class ApiCartItemsList(generic.ListView):

    def get(self, request, *args, **kwargs):
        items = CartItem.objects.all().values('product', 'quantity')
        data = list(items)
        return JsonResponse(data, safe=False)


class ApiCartItemDetail(generic.DetailView):
    model = CartItem
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        item = CartItem.objects.get(pk=kwargs['id'])
        data = model_to_dict(item)
        return JsonResponse(data, safe=False)


class ApiCartItemCreate(generic.CreateView):
    model = CartItem
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        self.object = None
        cart = ShoppingCart.objects.get(id=int(request.POST['cart']))
        product = Fruit.objects.get(id=int(request.POST['product']))
        quantity = int(request.POST['quantity'])
        added = cart.add_cart_item(product, quantity)
        cart_items = cart.get_cart_items()
        print('cart_items: ' + str(cart_items))
        if added:
            status = 201
        else:
            status = 409
        return JsonResponse(cart_items, safe=False, status=status)


class ApiCartItemDelete(generic.DeleteView):
    model = CartItem
    pk_url_kwarg = 'item_id'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        cart_item = CartItem.objects.get(pk=pk)
        user = ShopUser.objects.get(pk=self.request.user.id)
        if cart_item.cart.user.id != self.request.user.id:
            raise HttpResponse(status=401)
        self.cart = cart_item.cart
        return cart_item

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        cart = request.user.get_mycart()
        cart_items = cart.get_cart_items()
        print('cart_items: ' + str(cart_items))
        return JsonResponse(cart_items, safe=False, status=204)


class ApiCartItems(View):
    pk_url_kwarg = 'item_id'

    def get(self, request, *args, **kwargs):
        if len(kwargs) > 0:
            cart_item = CartItem.objects.get\
                (pk=kwargs['id'])
            if cart_item.cart.user.id != self.request.user.id:
                raise HttpResponse(status=401)
            data = model_to_dict(cart_item)
            return JsonResponse(data, safe=False)
        else:
            items = CartItem.objects.all().values('product', 'quantity')
            data = list(items)
            return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        self.object = None
        cart = ShoppingCart.objects.get(id=int(request.POST['cart']))
        if cart.user.id != self.request.user.id:
            raise HttpResponse(status=401)
        product = Fruit.objects.get(id=int(request.POST['product']))
        quantity = int(request.POST['quantity'])
        added = cart.add_cart_item(product, quantity)
        if added:
            status = 201
        else:
            status = 409
        return JsonResponse(self._cart_items(request), safe=False, status=status)

    def delete(self, request, *args, **kwargs):
        print('delete')
        pk = self.kwargs.get(self.pk_url_kwarg)
        cart_item = CartItem.objects.get(pk=pk)
        if cart_item.cart.user.id != self.request.user.id:
            raise HttpResponse(status=401)
        cart_item.delete()
        cart = request.user.get_mycart()
        cart_items = cart.get_cart_items()
        print(str(cart_items))
        return JsonResponse(cart_items, safe=False, status=200)

    def put(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, args, kwargs)
        return JsonResponse(status=403, data={'message': "access forbidden"})

    def _cart_items(self, request):
        cart = request.user.get_mycart()
        cart_items = cart.get_cart_items()
        print('cart_items: ' + str(cart_items))
        return cart_items


class ApiMyCart(ApiCartItems):

    def get(self, request, *args, **kwargs):
        cart_items = self._cart_items(request)
        return JsonResponse(cart_items, safe=False, status=200)



