from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from products.forms import FruitForm, FruitCategoryForm


class AjaxGeneral(generic.TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name, context=RequestContext(request))

    def dispatch(self, request, *args, **kwargs):
        #print('dispatch')
        return super(AjaxGeneral, self).dispatch(request, args, kwargs)


class AjaxFruitForm(AjaxGeneral):
    template_name = 'products/ajax_rest_form_fruit.html'

    def get(self, request, *args, **kwargs):
        context = {'form': FruitForm()}
        template = 'products/ajax_rest_form_fruit.html'
        return render(request, template, context)


class AjaxFruitEditForm(AjaxGeneral):

    def get(self, request, *args, **kwargs):
        context = {'form': FruitForm()}
        template = 'products/ajax_rest_form_edit_fruit.html'
        return render(request, template, context)


class AjaxFruitList(AjaxGeneral):

    def get(self, request, *args, **kwargs):
        template = 'products/ajax_rest_list_fruit.html'
        return render(request, template)


class AjaxFruitDetail(AjaxGeneral):

    def get(self, request, *args, **kwargs):
        template = 'products/ajax_rest_detail_fruit.html'
        return render(request, template)


class AjaxFruitCategoryForm(AjaxGeneral):

    def get(self, request, *args, **kwargs):
        context = {'form': FruitCategoryForm()}
        template = 'products/ajax_rest_form_fruit_category.html'
        return render(request, template, context)

