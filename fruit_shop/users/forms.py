from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ShopUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(ShopUserCreationForm, self).__init__(*args, **kwargs)
        # force email filed in
        # TODO: enforce email not null in model instead of in form
        self.fields['email'].required = True


class ShopUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
