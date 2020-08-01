from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from sells.forms import CartForm
from sells.models import ShoppingCart, Order


class OrderList(generic.ListView):
    model = Order
    fields = '__all__'


class CartSinglePage(generic.TemplateView):
    template_name = "sells/cart_rest_singlepage.html"


class AjaxCartForm(generic.TemplateView):
    template_name = 'sells/ajax_rest_form_cart.html'

    def get(self, request, *args, **kwargs):
        context = {'form': CartForm()}
        template = 'sells/ajax_rest_form_cart.html'
        return render(request, template, context)


class AjaxCartList(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        template = 'sells/ajax_rest_list_cart.html'
        return render(request, template)


class AjaxCartDetail(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        template = 'sells/ajax_rest_detail_cart.html'
        return render(request, template)


class AjaxMyCart(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        if request.user:
            template = 'sells/ajax_rest_cart.html'
            return render(request, template)

