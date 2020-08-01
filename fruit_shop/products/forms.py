from django.forms import ModelForm

from products.models import Fruit


class FruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = [
            'name',
            'sku',
            'stock_quantity',
            'weight_kg',
            'volume_l',
            'price',
            'category',
        ]
