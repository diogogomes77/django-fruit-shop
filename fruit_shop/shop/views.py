from django.views import generic


class ShopSinglePage(generic.TemplateView):
    template_name = "shop/shop_rest_singlepage.html"
