from django.db import models


class Product(models.Model):
    """
    Product is the abstract class for every product type
    this makes it possible to extend the product range in the future
    """
    name = models.CharField(max_length=100)
    sku = models.PositiveIntegerField()
    stock_quantity = models.PositiveIntegerField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    volume_l = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


class Fruit(Product):
    """
    Fruit is a product type
    """
    category = models.ForeignKey('FruitCategory', related_name="fruits", on_delete=models.CASCADE)


class FruitCategory(models.Model):
    """
    FruitCategory is the category where each fruit belongs
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
