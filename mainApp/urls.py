from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='homepage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)