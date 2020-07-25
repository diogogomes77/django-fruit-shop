from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import FormView

from users.forms import ShopUserCreationForm


class VisitorsOnly(FormView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseForbidden(render(request, "shop/403.html"))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseForbidden(reverse("shop/403.html"))
        return super().post(request, *args, **kwargs)


class SignUp(VisitorsOnly, generic.CreateView):
    form_class = ShopUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


class Login(VisitorsOnly, LoginView):
    template_name = 'users/login.html'

