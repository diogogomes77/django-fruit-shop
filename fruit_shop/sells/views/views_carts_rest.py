from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View, generic

from sells.models import ShoppingCart, CartItem


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
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        print('get_success_url')
        #return reverse_lazy('cart-api-list')
        return None


class ApiMyCart(View):

    def get(self, request, *args, **kwargs):
        if request.user:
            cart = request.user.get_mycart()
            data = model_to_dict(cart)
            items = []
            for item in data['items']:
                items.append(model_to_dict(item))
            data['items'] = items
            print('data= ' + str(data))
            return JsonResponse(data, safe=False)


class ApiCartItems(View):

    def get(self, request, *args, **kwargs):

        if len(kwargs) > 0:
            view = ApiCartItemDetail.as_view()
        else:
            view = ApiCartItemsList.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('ApiCartItems post')
        view = ApiCartItemCreate.as_view()
        return view(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
