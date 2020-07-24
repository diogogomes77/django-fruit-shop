from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ShopUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class ShopUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
