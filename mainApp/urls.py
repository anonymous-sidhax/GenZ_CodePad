from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='homepage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)