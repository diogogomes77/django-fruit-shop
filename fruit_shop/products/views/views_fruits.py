from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from products.forms import FruitForm
from products.models import Fruit
from products.views.views_utils import StaffOnly


class FruitList(generic.ListView):
    model = Fruit
    fields = '__all__'


class FruitCreate(StaffOnly, generic.CreateView):
    model = Fruit
    fields = '__all__'
    success_url = reverse_lazy('fruit-list')
    template_name = "products/fruit_form_rest.html"


class FruitUpdate(StaffOnly, generic.UpdateView):
    model = Fruit
    fields = '__all__'
    success_url = reverse_lazy('fruit-list')


class FruitDelete(StaffOnly, generic.DeleteView):
    model = Fruit
    success_url = reverse_lazy('fruit-list')

'''
def ajax_request(function):
    def wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            #return render_to_response('shop/ajax_required.html', {},
            #    context=RequestContext(request))
            render_to_response(request, 'shop/ajax_required.html', RequestContext(request).flatten())
        else:
            return function(request, *args, **kwargs)
    return wrapper
'''


class AjaxGeneral(generic.TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name, context=RequestContext(request))

    #@method_decorator(ajax_request)
    def dispatch(self, *args, **kwargs):
        #print('dispatch')
        return super(AjaxGeneral, self).dispatch(*args, **kwargs)


class FruitSinglePage(generic.TemplateView):
    template_name = "products/fruit_rest_singlepage.html"


class AjaxFruitForm(AjaxGeneral):
    template_name = 'products/ajax_rest_form_fruit.html'

    def get(self, request, *args, **kwargs):
        context = {'form': FruitForm()}
        template = 'products/ajax_rest_form_fruit.html'
        return render(request, template, context)


class AjaxFruitList(AjaxGeneral):

    def get(self, request, *args, **kwargs):
        template = 'products/ajax_rest_list_fruit.html'
        return render(request, template)


class AjaxFruitDetail(AjaxGeneral):

    def get(self, request, *args, **kwargs):
        template = 'products/ajax_rest_detail_fruit.html'
        return render(request, template)