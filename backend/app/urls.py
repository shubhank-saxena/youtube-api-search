from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import services, views

urlpatterns = [
    path('videos', views.GetVideos.as_view()),
    path('key', views.AddAPIKey.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
services.THREAD.start()
