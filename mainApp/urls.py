from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import index, about_us, runcode, process_speech, audio_test

urlpatterns = [
    path('', index, name='homepage'),
    path('about_us/', about_us, name='AboutUs'),
    path('runcode', runcode, name="runcode"),
    path('process_speech', process_speech, name="process_speech"),
    path('audio_test', audio_test, name="audio_test"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)