from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import index, about_us

urlpatterns = [
    path('', index, name='homepage'),
    path('about_us/', about_us, name='AboutUs'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)