from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.forms import model_to_dict


class CartItem(models.Model):
    """
        This is the intermediary table for Shopping Cart items relation with products
        having the quantity of products added to the cart
        Note: Product should be a generic relation to allow multiple product types
    """
    product = models.ForeignKey('products.Fruit',  on_delete=models.CASCADE)
    cart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()


class ShoppingCart(models.Model):
    """
        This is the Shopping cart where users will be adding products,
        each user should have a single active cart, not more than one active.
        The Shopping cart is active if there's no Order attached yet.
        A new Shopping cart is created when a first item is added to cart if
        user don't have an active cart yet.
    """
    user = models.ForeignKey('users.ShopUser', related_name='carts', on_delete=models.CASCADE)
    items = models.ManyToManyField(
        'products.Fruit',
        related_name='carts',
        through=CartItem,
        through_fields=('cart', 'product')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        """
        :return: a dict of the cart items to be used by Ajax
        """
        cart_items = self.items.through.objects.select_related('product').all()
        dict_cart = model_to_dict(self)
        items = []
        for item in cart_items:
            dict_item = model_to_dict(item)
            dict_item['product_id'] = item.product.id
            dict_item['name'] = item.product.name
            dict_item['price'] = item.product.price
            items.append(dict_item)
        dict_cart['items'] = items
        return dict_cart

    def add_cart_item(self, product, quantity=1):
        """
        :param quantity: Quantity of product
        :param product: The product to be added to the cart. It's stock_quantity is checked and updated
        :return: True if item was added. False if not
        """
        if product.stock_quantity < quantity:
            return False
        try:
            item = self.items.through.objects.get(product_id=product.id)
        except ObjectDoesNotExist:
            item = None
        print(str(item))
        if item:
            item.quantity += quantity
            item.save()
        else:
            self.items.through.objects.create(
                cart=self,
                product=product,
                quantity=quantity
            )
        product.stock_quantity -= quantity
        product.save()
        return True

    def del_cart_item(self, product):
        pass



class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.CharField(max_length=128)
    sku = models.SmallIntegerField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    volume_l = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.SmallIntegerField()


class Order(models.Model):
    """
        The Order is created when user checks out a Shopping Cart.
    """
    cart = models.ForeignKey('ShoppingCart', related_name='order', null=True, on_delete=models.SET_NULL)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
