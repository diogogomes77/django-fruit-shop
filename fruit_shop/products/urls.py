from django.urls import path

from products.views import AjaxFruitForm, AjaxFruitList, AjaxFruitDetail, AjaxFruitCategoryForm, AjaxFruitEditForm

urlpatterns = [
    path('ajax_get_fruit_form', AjaxFruitForm.as_view(), name='fruit-rest-form'),
    path('ajax_get_fruit_edit_form', AjaxFruitEditForm.as_view(), name='fruit-rest-form'),
    path('ajax_get_fruit_category_form', AjaxFruitCategoryForm.as_view(), name='fruit-category-rest-form'),
    path('ajax_get_fruit_list', AjaxFruitList.as_view(), name='fruit-rest-list'),
    path('ajax_get_fruit_detail', AjaxFruitDetail.as_view(), name='fruit-rest-detail'),
]


