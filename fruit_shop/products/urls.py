
from django.urls import path
from django.views.generic import TemplateView

from products.views import FruitList, FruitCreate, FruitUpdate, FruitDelete, FruitCategoryList, FruitCategoryCreate, \
    FruitCategoryUpdate, FruitCategoryDelete, FruitSinglePage, AjaxFruitForm

urlpatterns = [
    path('', FruitList.as_view(), name='fruit-list'),
    #path('rest/', TemplateView.as_view(template_name='products/fruit_list_rest.html'), name='fruit-rest'),
    path('rest/', FruitSinglePage.as_view(), name='fruit-rest'),
    path('rest/ajax_get_form', AjaxFruitForm.as_view(), name='fruit-rest-form'),

    path('add/', FruitCreate.as_view(), name='fruit-add'),

    path('<int:pk>/', FruitUpdate.as_view(), name='fruit-update'),
    path('<int:pk>/delete/', FruitDelete.as_view(), name='fruit-delete'),

    path('/fruit-categories', FruitCategoryList.as_view(), name='fruit_category-list'),
    path('/fruit-categories/add/', FruitCategoryCreate.as_view(), name='fruit_category-add'),
    path('/fruit-categories/<int:pk>/', FruitCategoryUpdate.as_view(), name='fruit_category-update'),
    path('/fruit-categories/<int:pk>/delete/', FruitCategoryDelete.as_view(), name='fruit_category-delete'),
]


