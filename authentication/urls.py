from django.urls import path
from .views import login, register, forget_password

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forget-password/', forget_password, name='forget_password'),
]