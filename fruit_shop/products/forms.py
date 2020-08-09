from django.forms import ModelForm

from products.models import Fruit, FruitCategory


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


class FruitCategoryForm(ModelForm):
    class Meta:
        model = FruitCategory
        fields = [
            'name',
        ]