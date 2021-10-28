from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import homePageView, login, register, forget_password

urlpatterns = [
    path('', homePageView, name='homepage'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forget_password/', forget_password, name='forget_password'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)