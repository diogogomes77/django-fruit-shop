from django import forms

from users.models import Customer


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username', 'email', 'password1','password2')
