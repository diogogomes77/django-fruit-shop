from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from users.forms import ShopUserCreationForm


class SignUp(generic.CreateView):
    form_class = ShopUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Login(LoginView):
    template_name = 'login.html'

