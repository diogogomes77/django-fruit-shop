
from django.urls import path, include

from users import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]
