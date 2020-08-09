from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),

    path('products/', include('products.urls')),
    path('api/products/', include('products.urls-rest')),

    path('sells/', include('sells.urls')),
    path('api/sells/', include('sells.urls-rest')),
    path('api/carts/', include('sells.urls-carts-rest')),

    path('', include('shop.urls')),

] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
