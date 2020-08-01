from django.forms import ModelForm

from sells.models import ShoppingCart


class CartForm(ModelForm):
    class Meta:
        model = ShoppingCart
        fields = [
            'user',
            'items',
        ]
