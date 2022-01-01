from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import index, about_us, runcode, process_speech

urlpatterns = [
    path('', index, name='homepage'),
    path('about_us/', about_us, name='AboutUs'),
    path('runcode', runcode, name="runcode"),
    path('process_speech', process_speech, name="process_speech"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)